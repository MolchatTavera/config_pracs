def assemble_load_constant(A, B):
    # Команда загрузки константы имеет размер 5 байт
    opcode = A & 0xFF  # Убедимся, что A помещается в 1 байт
    B_bytes = B.to_bytes(4, byteorder='little', signed=False)
    instruction = bytes([opcode]) + B_bytes
    return instruction

def assemble_read_memory(A, B):
    # Команда чтения значения из памяти имеет размер 3 байта
    opcode = A & 0xFF
    B &= 0x3FF  # Убедимся, что B занимает только 10 бит
    B_bytes = B.to_bytes(2, 'little')
    instruction = bytes([opcode]) + B_bytes
    return instruction

def assemble_write_memory(A, B):
    # Команда записи значения в память имеет размер 3 байта
    opcode = A & 0xFF
    B &= 0x3FF
    B_bytes = B.to_bytes(2, 'little')
    instruction = bytes([opcode]) + B_bytes
    return instruction

def assemble_unary_not(A, B):
    # Унарная операция: побитовое "не" имеет размер 3 байта
    opcode = A & 0xFF
    B &= 0x1FF  # Убедимся, что B занимает только 9 бит
    B_bytes = B.to_bytes(2, 'little')
    instruction = bytes([opcode]) + B_bytes
    return instruction

# Тесты

# Тест для загрузки константы (A=45, B=755)
instruction_load_const = assemble_load_constant(45, 755)
print(', '.join(f'0x{byte:02X}' for byte in instruction_load_const))
# Ожидаемый вывод: 0x2D, 0xF3, 0x02, 0x00, 0x00

# Тест для чтения значения из памяти (A=57, B=312)
instruction_read_memory = assemble_read_memory(57, 312)
print(', '.join(f'0x{byte:02X}' for byte in instruction_read_memory))
# Ожидаемый вывод: 0x39, 0x38, 0x01

# Тест для записи значения в память (A=205, B=220)
instruction_write_memory = assemble_write_memory(205, 220)
print(', '.join(f'0x{byte:02X}' for byte in instruction_write_memory))
# Ожидаемый вывод: 0xCD, 0xDC, 0x00

# Тест для унарной операции побитовое "не" (A=85, B=94)
instruction_unary_not = assemble_unary_not(85, 94)
print(', '.join(f'0x{byte:02X}' for byte in instruction_unary_not))
# Ожидаемый вывод: 0x55, 0x5E, 0x00