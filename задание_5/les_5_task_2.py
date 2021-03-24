"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] 
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, 
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. 
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной 
задаче под запретом."""

from collections import Counter

first = input().upper() 
second = input().upper() 

hex_map = Counter({'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15})
if len(first) > len(second):
    first, second = second, first
second = second[::-1]
third = []
j = -1
k = 0
for i in second:
    one = hex_map[i]
    two = hex_map[first[j]]
    third.append(hex_map[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
    j -= 1
    if j == -len(first)-1:
        break
diff = len(second) - len(first)

if diff:
    for i in second[-diff:]:
        third.append(hex_map[(hex_map.index(second[-diff])+k)%16])
        if hex_map[second[-diff]]+1 >=15:
            k = 1
        else:
            k = 0
if k == 1:
    third.append('1')

print(third[::-1])

