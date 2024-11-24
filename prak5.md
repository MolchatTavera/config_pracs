# Конфигурационное управление практическое задание номер 4
### Лысогорский Михаил Сергеевич ИКБО-62-23

# Задание 1
Байткод:
```
11          0 LOAD_FAST                0 (x)
            2 LOAD_CONST               1 (10)
            4 BINARY_MULTIPLY
            6 LOAD_CONST               2 (42)
            8 BINARY_ADD
           10 RETURN_VALUE
```
эквивалентное выражение на Python:
```
def foo(x):
    return x * 10 + 42
```

# Задание 2
Байт-код представляет собой функцию, вычисляющую *факториал числа*.
```
0  LOAD_CONST       1 (1)        — Загружает константу 1.
2  STORE_FAST       1 (r)        — Сохраняет 1 в переменную `r`.
4  LOAD_FAST        0 (n)        — Загружает значение переменной `n`.
6  LOAD_CONST       1 (1)        — Загружает константу 1.
8  COMPARE_OP       4 (>)        — Сравнивает `n > 1`.
10 POP_JUMP_IF_FALSE 30           — Если `n <= 1`, переходит к адресу 30.
12 LOAD_FAST        1 (r)        — Загружает значение `r`.
14 LOAD_FAST        0 (n)        — Загружает значение `n`.
16 INPLACE_MULTIPLY              — Выполняет `r *= n`.
18 STORE_FAST       1 (r)        — Сохраняет результат в `r`.
20 LOAD_FAST        0 (n)        — Загружает значение `n`.
22 LOAD_CONST       1 (1)        — Загружает константу 1.
24 INPLACE_SUBTRACT              — Выполняет `n -= 1`.
26 STORE_FAST       0 (n)        — Сохраняет результат в `n`.
28 JUMP_ABSOLUTE    4             — Переходит к адресу 4 (начало цикла).
30 LOAD_FAST        1 (r)        — Загружает значение `r`.
32 RETURN_VALUE                   — Возвращает значение `r`.
```

# Задание 3
# №1
Java-код функции:
```
public int foo(int x) {
    return x * 10 + 42;
}
```
Байткод функции foo:
```
0: iload_1       
1: bipush        10    
3: imul         
4: bipush        42    
6: iadd         
7: ireturn      
```
# №2

Java-код функции:
```
public int factorial(int n) {
    int r = 1;
    while (n > 1) {
        r *= n;
        n -= 1;
    }
    return r;
}
```
Байткод функции factorial:
```
0:  iconst_1      
1:  istore_2      
2:  iload_1       
3:  iconst_1      
4:  if_icmple     17
7:  iload_2       
8:  iload_1       
9:  imul          
10: istore_2      
11: iload_1       
12: iconst_1      
13: isub          
14: istore_1      
15: goto          2
17: iload_2       
18: ireturn
```    
# Задание 4
```  


```
# Задание 5
```

```


