# Задание 1
``` 

cut -d: -f1 /etc/passwd | sort

```

![1](https://github.com/user-attachments/assets/21280eb1-f99d-4956-80f9-6c73cfe17cbe)

# Задание 2
```  
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -n 5

```

![2](https://github.com/user-attachments/assets/1248b167-7ff5-4533-bafb-9c31e64dfa25)

# Задание 3
```  
text="Hello from RTU MIREA!"; text_length=${#text}; border=$(printf "+-%${text_length}s-+" "" | tr " " "-"); echo "$border"; echo "| $text |"; echo "$border"

```

![3](https://github.com/user-attachments/assets/5114a075-156b-491a-a0ff-741314cdb6b3)

# Задание 4
```  
grep -o -E '\b[_a-zA-Z][_a-zA-Z0-9]*\b' hello.c | uniq

```
![4](https://github.com/user-attachments/assets/2779dc2e-e6bf-4d6c-b373-84ccb1619c2f)

# Задание 5
```  
#!/bin/bash

program_name="$1"

if [ ! -f "$program_name" ]; then
    echo "Ошибка: $program_name не найден!"
    exit 1
fi

chmod +x "$program_name"

sudo cp "$program_name" /usr/local/bin/

sudo chmod 755 /usr/local/bin/"$program_name"

echo "Файл $program_name успешно зарегистрирован в /usr/local/bin."

```
![{15669DF7-0E89-4C12-9C85-58B920249686}](https://github.com/user-attachments/assets/c2611742-56f8-4cce-b8b5-9033357d65be)

# Задание 6
``` 
#!/bin/bash

for file in *.c *.js *.py; do
    if [ -f "$file" ]; then
        first_line=$(head -n 1 "$file")
        if [[ "$first_line" =~ ^//.* ]] || [[ "$first_line" =~ ^#.* ]] || [[ "$first_line" =~ ^/\*.* ]]; then
            echo "В файле $file есть комментарий в первой строке."
        else
            echo "В файле $file нет комментария в первой строке."
        fi
    fi
done

```
![{D15B5E72-F5A5-42CD-8B0C-D4288CE23CB4}](https://github.com/user-attachments/assets/100fda80-ae52-47a8-ad00-ab23dbb3539d)

# Задание 7
``` 
#!/bin/bash

declare -A file_hashes

find "$1" -type f | while read -r file; do
    hash=$(sha256sum "$file" | awk '{print $1}')
   
    if [[ -n "${file_hashes[$hash]}" ]]; then
        echo "Найден дубликат: $file и ${file_hashes[$hash]}"
    else
        file_hashes[$hash]="$file"
    fi
done
```
![{1C14231F-CF6C-431D-9C58-806EA82BFD5A}](https://github.com/user-attachments/assets/e020a3c9-8a91-4498-9125-8cbd6a557add)

# Задание 8
``` 
#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <путь_к_каталогу> <расширение>"
    exit 1
fi

directory="$1"
extension="$2"

if [ ! -d "$directory" ]; then
    echo "Указанный каталог не существует."
    exit 1
fi

files=$(find "$directory" -type f -name "*.$extension")

if [ -z "$files" ]; then
    echo "Нет файлов с расширением .$extension в каталоге $directory."
    exit 0
fi

archive_name="archived_files_$(date +%Y%m%d_%H%M%S).tar"
tar -cvf "$archive_name" $files

echo "Файлы с расширением .$extension успешно архивированы в $archive_name."

```
![{07DE91B3-0F64-4C3F-8B8E-23913ABE1C8B}](https://github.com/user-attachments/assets/5bb7eca2-60e9-4205-96a6-acf9bb573b2f)



# Задание 9
``` 
#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <входной_файл> <выходной_файл>"
    exit 1
fi

input_file="$1"
output_file="$2"

if [ ! -f "$input_file" ]; then
    echo "Входной файл не существует."
    exit 1
fi

sed 's/    /\t/g' "$input_file" > "$output_file"

echo "Замена 4 пробелов на табуляцию завершена. Результат сохранен в $output_file."

```
![{0C33339B-4631-4371-B414-41E370258A9C}](https://github.com/user-attachments/assets/04eaaae4-df83-4eb8-a006-e4d69c6e3361)


# Задание 10
``` 
#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Использование: $0 <путь_к_директории>"
    exit 1
fi

directory="$1"

if [ ! -d "$directory" ]; then
    echo "Указанная директория не существует."
    exit 1
fi

find "$directory" -type f -name "*.txt" -empty
```
![{8E6CE197-1443-4641-A0A5-4EC1D4F62FAC}](https://github.com/user-attachments/assets/6d77f6c7-f954-4846-ac99-8cb4f6023417)

