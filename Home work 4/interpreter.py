import sys
import struct
import xml.etree.ElementTree as ET

MEMORY_SIZE = 65536  # Размер памяти УВМ увеличен для поддержки адресов до 65535

def interpret_file(binary_file, result_file, mem_range):
    with open(binary_file, 'rb') as f:
        code = f.read()

    memory = [0] * MEMORY_SIZE
    accumulator = 0
    pc = 0  # Program counter

    code_length = len(code)

    while pc < code_length:
        opcode = code[pc]
        if opcode == 45:  # LOAD_CONST
            if pc + 5 > code_length:
                raise ValueError('Недостаточно данных для LOAD_CONST')
            B = struct.unpack_from('<I', code, pc + 1)[0]
            accumulator = B
            pc += 5
        elif opcode == 57:  # READ_MEM
            if pc + 3 > code_length:
                raise ValueError('Недостаточно данных для READ_MEM')
            B_bytes = code[pc + 1:pc + 3]
            B = int.from_bytes(B_bytes, 'little')
            accumulator = memory[B]
            pc += 3
        elif opcode == 205:  # WRITE_MEM
            if pc + 3 > code_length:
                raise ValueError('Недостаточно данных для WRITE_MEM')
            B_bytes = code[pc + 1:pc + 3]
            B = int.from_bytes(B_bytes, 'little')
            memory[B] = accumulator
            pc += 3
        elif opcode == 85:  # NOT
            if pc + 3 > code_length:
                raise ValueError('Недостаточно данных для NOT')
            B_bytes = code[pc + 1:pc + 3]
            B = int.from_bytes(B_bytes, 'little')
            address = (accumulator + B) % MEMORY_SIZE
            value = memory[address]
            accumulator = (~value) & 0xFFFFFFFF  # 32-битное беззнаковое значение
            pc += 3
        elif opcode == 0:  # HALT
            pc += 1
            break
        else:
            raise ValueError(f"Неизвестная команда {opcode} на позиции {pc}")

    # Сохранение результатов памяти
    mem_start, mem_end = map(int, mem_range.split('-'))
    root = ET.Element('MemoryDump')
    for addr in range(mem_start, mem_end + 1):
        mem_elem = ET.SubElement(root, 'Memory', Address=str(addr))
        value = memory[addr] & 0xFFFFFFFF  # Убедимся, что значение беззнаковое 32-битное
        mem_elem.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(result_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Интерпретатор для УВМ')
    parser.add_argument('binary_file', help='Путь к бинарному файлу')
    parser.add_argument('--result_file', default='result.xml', help='Путь к файлу результата (XML)')
    parser.add_argument('--mem_range', default='1000-1005', help='Диапазон памяти для вывода (например, 1000-1005)')
    args = parser.parse_args()

    interpret_file(args.binary_file, args.result_file, args.mem_range)