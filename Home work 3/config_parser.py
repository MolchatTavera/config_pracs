import sys
import json
import re

def parse_value(token, variables):
    token = token.strip()
    if token.startswith('(list'):
        return parse_list(token, variables)
    elif token.startswith('#{'):
        return parse_variable(token, variables)
    elif re.match(r'^\d+$', token):
        return int(token)
    else:
        raise ValueError(f"Неправильное значение: {token}")

def parse_list(text, variables):
    if not text.endswith(')'):
        raise ValueError("Ожидается ')' в конце списка.")
    content = text[5:-1].strip()  # Убираем '(list' и ')'
    items = []
    depth = 0
    token = ''
    for char in content:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if char.isspace() and depth == 0:
            if token:
                items.append(parse_value(token, variables))
                token = ''
        else:
            token += char
    if token:
        items.append(parse_value(token, variables))
    return items

def parse_variable(token, variables):
    match = re.match(r'^#\{([a-z]+)\}$', token)
    if match:
        var_name = match.group(1)
        if var_name in variables:
            return variables[var_name]
        else:
            raise ValueError(f"Неизвестная переменная: {var_name}")
    else:
        raise ValueError(f"Неправильное использование переменной: {token}")

def main():
    variables = {}
    data = sys.stdin.read()
    lines = data.strip().split('\n')
    results = []
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):  # Пропускаем пустые строки и комментарии
            continue
        if line.startswith('var'):
            # Обработка объявления переменной
            match = re.match(r'^var\s+([a-z]+)\s*=\s*(.+)$', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2)
                try:
                    variables[var_name] = parse_value(var_value, variables)
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}: {e}", file=sys.stderr)
                    sys.exit(1)
            else:
                print(f"Синтаксическая ошибка в строке {line_num}: {line}", file=sys.stderr)
                sys.exit(1)
        else:
            # Обработка значения
            try:
                result = parse_value(line, variables)
                results.append(result)
            except ValueError as e:
                print(f"Ошибка в строке {line_num}: {e}", file=sys.stderr)
                sys.exit(1)
    json_output = json.dumps(results, ensure_ascii=False, indent=2)
    print(json_output)

if __name__ == "__main__":
    main()