# Конфигурационное управление практическое задание номер 4
### Лысогорский Михаил Сергеевич ИКБО-62-23

# Задание 1

![{0847DBA7-3A83-4C37-BF15-D03B52CF4BE4}](https://github.com/user-attachments/assets/38369287-de16-4aa5-a968-c9ffaa0f8da9)




# Задание 2
```
$ git init
Initialized empty Git repository in /path/to/your/repository/.git/

$ git config user.name "coder1"
$ git config user.email "osma12345@yandex.ru"

$ echo "print('Hello, World!')" > prog.py

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        prog.py

nothing added to commit but untracked files present (use "git add" to track)

$ git add prog.py

$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   prog.py

$ git commit -m "Добавляем prog.py с начальным содержимым"
[master (root-commit) a1b2c3d] Добавить prog.py с начальным содержимым
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

$ git log
commit a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwx (HEAD -> master)
Author: coder1 <osma12345@yandex.ru>
Date:   Thu Apr 27 10:00:00 2024 +0300

```


# Задание 3
```  
mkdir my_project
cd my_project
git init
git config user.name "coder1"
git config user.email "osma12345@yandex.ru"
echo "print('Hello, Git!')" > prog.py
git add prog.py
git commit -m "Добавить prog.py с начальным содержимым"
git init --bare server.git
git remote add server ./server.git
git remote -v
git push -u server master
git pull server master
cd ..
git clone my_project/server.git coder2-repo
cd coder2-repo
git config user.name "coder2"
git config user.email "osma14@yandex.ru"
echo "# Описание программы" > readme.md
git add readme.md
git commit -m "Добавить readme.md с описанием программы"
git push
git pull server master
git add readme.md
git commit -m "Добавить информацию о coder2 в readme.md и решить конфликт"
git push server master

git log --graph --oneline --all
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: coder2 <osma14@yandex.ru>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: coder1 <osma12345@yandex.ru>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: coder2 <osma14@yandex.ru>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: coder2 <osma14@yandex.ru>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: coder1 <osma12345@yandex.ru>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit


```



# Задание 4
```  
import subprocess

def get_git_objects():
    result = subprocess.run(['git', 'rev-list', '--all', '--objects'], capture_output=True, text=True)
    objects = result.stdout.strip().split('\n')
    return [obj.split()[0] for obj in objects if obj]

def show_object_content(object_hash):
    result = subprocess.run(['git', 'cat-file', '-p', object_hash], capture_output=True, text=True)
    return result.stdout

def main():
    objects = get_git_objects()
    for obj_hash in objects:
        print(f"--- Object {obj_hash} ---")
        content = show_object_content(obj_hash)
        print(content)
        print("\n")

if __name__ == "__main__":
    main()


```
```
--- Object 227d84c89e60e09eebbce6c0b94b41004a4541a4 ---
tree 827efc6d56897b048c772eb4087f854f46256132
100644 blob ba9dfe9cb24316694808a347e8c36f8383d81bbe    prog.py

--- Object ba9dfe9cb24316694808a347e8c36f8383d81bbe ---
blob content of prog.py:
print('Hello, Git!')

--- Object 48ce28336e6b3b983cbd6323500af8ec598626f1 ---
commit 48ce28336e6b3b983cbd6323500af8ec598626f1
Author: coder2 <osma14@yandex.ru>
Date:   Sun Oct 11 11:24:00 2020 +0300

    coder2 info

--- Object d731ba84014d603384cc3287a8ea9062dbb92303 ---
commit d731ba84014d603384cc3287a8ea9062dbb92303
Author: coder1 <osma12345@yandex.ru>
Date:   Sun Oct 11 11:22:52 2020 +0300

    coder1 info

--- Object a457d748f0dab75b4c642e964172887de3ef4e3e ---
commit a457d748f0dab75b4c642e964172887de3ef4e3e
Merge: 48ce283 d731ba8
Author: coder2 <osma14@yandex.ru>
Date:   Sun Oct 11 11:27:09 2020 +0300

    readme fix

--- Object 227d84c89e60e09eebbce6c0b94b41004a4541a4 ---
commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
Author: coder1 <osma12345@yandex.ru>
Date:   Sun Oct 11 11:11:46 2020 +0300

    first commit
```

