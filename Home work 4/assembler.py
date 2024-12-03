import sys
import struct
import xml.etree.ElementTree as ET

def assemble_instruction(line):
    # Игнорируем комментарии и пустые строки
    line = line.split(';')[0].strip()
    if not line:
        return None  # Исправлено: возвращаем None вместо (None, None)
    parts = line.strip().split()
    opcode = parts[0].upper()
    args = parts[1:]
    instruction_bytes = b''
    log_data = {}

    if opcode == 'LOAD_CONST':
        # Syntax: LOAD_CONST value
        if len(args) != 1:
            raise ValueError('LOAD_CONST требует 1 аргумент')
        A = 45  # opcode for LOAD_CONST
        B = int(args[0])
        opcode_byte = A & 0xFF
        B_bytes = struct.pack('<I', B & 0xFFFFFFFF)
        instruction_bytes = bytes([opcode_byte]) + B_bytes
        log_data = {'opcode': 'LOAD_CONST', 'A': A, 'B': B}

    elif opcode == 'READ_MEM':
        # Syntax: READ_MEM address
        if len(args) != 1:
            raise ValueError('READ_MEM требует 1 аргумент')
        A = 57  # opcode for READ_MEM
        B = int(args[0]) & 0xFFFF  # Увеличиваем до 16 бит для поддержки адресов до 65535
        opcode_byte = A & 0xFF
        B_bytes = B.to_bytes(2, 'little')
        instruction_bytes = bytes([opcode_byte]) + B_bytes
        log_data = {'opcode': 'READ_MEM', 'A': A, 'B': B}

    elif opcode == 'WRITE_MEM':
        # Syntax: WRITE_MEM address
        if len(args) != 1:
            raise ValueError('WRITE_MEM требует 1 аргумент')
        A = 205  # opcode for WRITE_MEM
        B = int(args[0]) & 0xFFFF  # Увеличиваем до 16 бит для поддержки адресов до 65535
        opcode_byte = A & 0xFF
        B_bytes = B.to_bytes(2, 'little')
        instruction_bytes = bytes([opcode_byte]) + B_bytes
        log_data = {'opcode': 'WRITE_MEM', 'A': A, 'B': B}

    elif opcode == 'NOT':
        # Syntax: NOT offset
        if len(args) != 1:
            raise ValueError('NOT требует 1 аргумент')
        A = 85  # opcode for NOT
        B = int(args[0]) & 0xFFFF  # Увеличиваем до 16 бит для поддержки больших смещений
        opcode_byte = A & 0xFF
        B_bytes = B.to_bytes(2, 'little')
        instruction_bytes = bytes([opcode_byte]) + B_bytes
        log_data = {'opcode': 'NOT', 'A': A, 'B': B}

    elif opcode == 'HALT':
        # Syntax: HALT
        A = 0  # opcode for HALT
        instruction_bytes = bytes([A])
        log_data = {'opcode': 'HALT', 'A': A}

    else:
        raise ValueError(f'Неизвестная команда: {opcode}')

    # Выводим байты инструкции для проверки
    print(', '.join(f'0x{byte:02X}' for byte in instruction_bytes))

    return instruction_bytes, log_data

def assemble_file(input_file, output_file, log_file):
    # Открываем файл с указанием кодировки UTF-8
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    binary_code = b''
    root = ET.Element('Log')

    for line in lines:
        result = assemble_instruction(line)
        if result is not None:
            instruction_bytes, log_data = result
            binary_code += instruction_bytes
            instr_elem = ET.SubElement(root, 'Instruction')
            for key, value in log_data.items():
                ET.SubElement(instr_elem, key).text = str(value)
        else:
            # Если результат None, пропускаем эту строку
            continue

    with open(output_file, 'wb') as f_out:
        f_out.write(binary_code)

    tree = ET.ElementTree(root)
    tree.write(log_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Ассемблер для УВМ')
    parser.add_argument('input_file', help='Путь к файлу исходного кода на ассемблере')
    parser.add_argument('output_file', help='Путь к выходному бинарному файлу')
    parser.add_argument('--log_file', default='assemble_log.xml', help='Путь к файлу лога (XML)')
    args = parser.parse_args()

    assemble_file(args.input_file, args.output_file, args.log_file)