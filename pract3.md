# Конфигурационное управление практическое задание номер 3
### Лысогорский Михаил Сергеевич ИКБО-62-23

# Задание 1
``` 

{
  groups: [ 
    'ИКБО-' + std.toString(n) + '-20' for n in std.range(1, 24) 
  ],

  local student(name, age, group) = {
    name: name,
    age: age,
    group: group,
  },

  students: [
    student("Иванов И.И.", 19, "ИКБО-10-23"),
    student("Петров П.П.", 18, "ИКБО-42-23"),
    student("Сидоров С.С.", 20, "ИКБО-22-23"),
    student("Лысогорский М.С..", 18, "ИКБО-62-23") 
  ],

  subject: "Конфигурационное управление"
}


```

![{4CF31F79-ABDA-43DC-AA5B-7E23F638389F}](https://github.com/user-attachments/assets/8e30e717-302b-4265-bf34-593e74acda92)

# Задание 2
```  
let mkGroup = \(n : Natural) -> "ИКБО-${Natural/show n}-20"

let groups = 
      [ mkGroup 1
      , mkGroup 2
      , mkGroup 3
      , mkGroup 4
      , mkGroup 5
      , mkGroup 6
      , mkGroup 7
      , mkGroup 8
      , mkGroup 9
      , mkGroup 10
      , mkGroup 11
      , mkGroup 12
      , mkGroup 13
      , mkGroup 14
      , mkGroup 15
      , mkGroup 16
      , mkGroup 17
      , mkGroup 18
      , mkGroup 19
      , mkGroup 20
      , mkGroup 21
      , mkGroup 22
      , mkGroup 23
      , mkGroup 24
      ]

let Student = { age : Natural, group : Text, name : Text }

let student =
      \(name : Text) ->
      \(age : Natural) ->
      \(group : Text) ->
        { name = name, age = age, group = group } : Student

let students =
      [ student "Иванов И.И." 19 "ИКБО-10-23"
      , student "Петров П.П." 18 "ИКБО-42-23"
      , student "Сидоров С.С." 20 "ИКБО-22-23"
      , student "Лысогорский М.С." 18 "ИКБО-62-23"
      ]

let subject = "Конфигурационное управление"

in  { groups = groups, students = students, subject = subject }



```

![{D7C64FAF-E891-4181-B32D-42244B649B9C}](https://github.com/user-attachments/assets/90eb5c69-a516-4e3c-abfc-75b769af1c16)


# Задание 3
Пример грамматики в BNF:
```  
E = '0' | '1' | E '0' | E '1'

```
Пример на Python:
```  
BNF = """
E = 0 | 1 | 0 E | s1 E
"""
```
![image](https://github.com/MolchatTavera/configuration-management-practical-work-number-1/pract3/pic3.1.png)

# Задание 4
Пример грамматики в BNF:
```  
E = | '(' E ')' | '{' E '}' | E E

```
Пример на Python:
```  
BNF = '''
E = | ( E ) | { E } | E E
'''
```
![image](https://github.com/MolchatTavera/configuration-management-practical-work-number-1/pract3/pic3.2.png)

# Задание 5
Пример грамматики в BNF:
```  
E  = T | E '|' T
T  = F | T '&' F
F  = 'x' | 'y' | '~' G | G
G  = '(' E ')' | 'x' | 'y'

```
Пример на Python:
```  
BNF = '''
E = T | E '|' T
T = F | T '&' F
F = x | y | ~ G | G
G = ( E ) | x | y
'''
```
![image](https://github.com/MolchatTavera/configuration-management-practical-work-number-1/pract3/pic3.3.png)

