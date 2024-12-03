import argparse
import os
import urllib.request
import gzip
import shutil
import subprocess

def download_packages_file(repo_url, distro='focal', arch='amd64'):
    """
    Загружает файл Packages.gz из указанного репозитория Ubuntu.
    """
    packages_url = f"{repo_url}/dists/{distro}/main/binary-{arch}/Packages.gz"
    packages_gz = 'Packages.gz'
    packages_txt = 'Packages'

    print(f"Загрузка файла Packages с {packages_url}...")
    urllib.request.urlretrieve(packages_url, packages_gz)

    print("Распаковка Packages.gz...")
    with gzip.open(packages_gz, 'rb') as f_in:
        with open(packages_txt, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.remove(packages_gz)
    return packages_txt

def parse_packages_file(packages_file):
    """
    Парсит файл Packages и возвращает словарь пакетов и их зависимостей.
    """
    packages = {}
    package_info = {}
    print("Парсинг файла Packages...")
    with open(packages_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                # Пустая строка, конец описания пакета
                if 'Package' in package_info:
                    package_name = package_info['Package']
                    deps = []
                    for dep_field in ['Depends', 'Pre-Depends']:
                        if dep_field in package_info:
                            deps += parse_dependencies(package_info[dep_field])
                    packages[package_name] = deps
                package_info = {}
            elif line.startswith(' '):
                # Продолжение предыдущего поля
                if 'last_field' in package_info:
                    package_info[package_info['last_field']] += ' ' + line.strip()
            else:
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    package_info[key] = value
                    package_info['last_field'] = key
        # Обработка последнего пакета в файле
        if 'Package' in package_info:
            package_name = package_info['Package']
            deps = []
            for dep_field in ['Depends', 'Pre-Depends']:
                if dep_field in package_info:
                    deps += parse_dependencies(package_info[dep_field])
            packages[package_name] = deps

    os.remove(packages_file)
    return packages

def parse_dependencies(deps_str):
    """
    Парсит строку с зависимостями и возвращает список имен пакетов.
    """
    dependencies = []
    for dep in deps_str.split(','):
        dep = dep.strip()
        # Обработка альтернативных зависимостей
        alternatives = dep.split('|')
        for alt in alternatives:
            alt = alt.strip()
            # Убираем информацию о версиях и дополнительные данные
            alt = alt.split('(', 1)[0].strip()
            # Удаляем кавычки и проблемные символы
            alt = alt.replace('"', '').replace("'", '').replace('\\', '').replace('\n', '').replace('\r', '')
            dependencies.append(alt)
            break  # Берем только первый альтернативный вариант
    return dependencies

def build_dependency_graph(packages_dict, package_name, max_depth):
    """
    Строит граф зависимостей в нотации Mermaid с использованием безопасных идентификаторов узлов.
    """
    graph_lines = ['graph LR']
    visited = set()
    node_ids = {}
    node_counter = [0]

    def get_node_id(name):
        if name not in node_ids:
            node_ids[name] = f'node{node_counter[0]}'
            node_counter[0] += 1
        return node_ids[name]

    def sanitize_label(label):
        # Экранируем проблемные символы
        return label.replace('"', '\\"').replace("'", "\\'").replace('\n', '').replace('\r', '')

    def add_edges(pkg_name, depth):
        if depth > max_depth or pkg_name in visited:
            return
        visited.add(pkg_name)
        dependencies = packages_dict.get(pkg_name, [])
        current_node_id = get_node_id(pkg_name)
        current_label = sanitize_label(pkg_name)
        graph_lines.append(f'    {current_node_id}["{current_label}"]')
        for dep in dependencies:
            if dep:
                dep_node_id = get_node_id(dep)
                dep_label = sanitize_label(dep)
                graph_lines.append(f'    {dep_node_id}["{dep_label}"]')
                graph_lines.append(f'    {current_node_id} --> {dep_node_id}')
                add_edges(dep, depth + 1)

    print(f"Построение графа зависимостей для пакета '{package_name}' до глубины {max_depth}...")
    add_edges(package_name, 1)
    return '\n'.join(graph_lines)

def render_mermaid_graph(mermaid_code, output_path, mmdc_path):
    """
    Использует Mermaid CLI для рендеринга графа в файл PNG.
    """
    mermaid_file = 'graph.mmd'
    with open(mermaid_file, 'w', encoding='utf-8') as f:
        f.write(mermaid_code)
    
    print("Рендеринг графа в PNG...")
    # Формируем команду как строку для shell=True
    cmd = f'"{mmdc_path}" -i "{mermaid_file}" -o "{output_path}"'

    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при рендеринге графа: {e.stderr}")
    finally:
        if os.path.exists(mermaid_file):
            os.remove(mermaid_file)

def main():
    parser = argparse.ArgumentParser(description='Визуализатор зависимостей пакетов Ubuntu')
    parser.add_argument('--graphviz-path', required=False, help='Путь к исполняемому файлу Mermaid CLI (mmdc)')
    parser.add_argument('--package-name', required=True, help='Имя пакета для анализа')
    parser.add_argument('--output-path', required=True, help='Путь для сохранения изображения графа зависимостей (PNG)')
    parser.add_argument('--max-depth', type=int, required=True, help='Максимальная глубина анализа зависимостей')
    parser.add_argument('--repo-url', required=True, help='URL-адрес репозитория Ubuntu')

    args = parser.parse_args()

    # Если путь к mmdc не указан, используем 'mmdc' из PATH
    mmdc_path = args.graphviz_path if args.graphviz_path else 'mmdc'

    packages_file = download_packages_file(args.repo_url)
    packages_dict = parse_packages_file(packages_file)
    if args.package_name not in packages_dict:
        print(f"Пакет '{args.package_name}' не найден в репозитории.")
        return

    mermaid_code = build_dependency_graph(packages_dict, args.package_name, args.max_depth)
    
    # Выводим сгенерированный код Mermaid для отладки
    print("Сгенерированный код Mermaid:")
    print(mermaid_code)
    
    render_mermaid_graph(mermaid_code, args.output_path, mmdc_path)

    print("Граф зависимостей успешно сгенерирован и сохранен в формате PNG.")

if __name__ == '__main__':
    main()