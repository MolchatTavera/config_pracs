# Создайте структуру каталогов и файлов:

```
mkdir ~/vfs
cd ~/vfs
mkdir Documents
mkdir Pictures
echo "This is a test file." > Documents/test.txt
echo "Hello, World!" > hello.txt
echo "Sample Image Content" > Pictures/image.jpg

```
# Создание tar-архива:
```
cd ~
tar -cvf virtual_fs.tar -C vfs .

```
# Проверьте содержимое архива:
```
tar -tf ./virtual_fs.tar

```
# Запуск эмулятора:
```
python3 emulator.py config.xml

```
# Проверка команд 
![{7EC6DE07-2CC4-47E5-BD93-3A19FF4ECAE5}](https://github.com/user-attachments/assets/08de35ac-4565-4acd-8980-c436162f05d0)

