"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать."""

from random import randint

number_list = [randint(-20,20) for i in range(20)]
print(number_list)
min_list = [0,100]
max_list = [0,-100]
for i in range(len(number_list)):
    if number_list[i] > max_list[1]:
        max_list[0] = i
        max_list[1] = number_list[i]
    if number_list[i] < min_list[1]:
        min_list[0] = i
        min_list[1] = number_list[i]
print(f"max = {max_list}")
print(f"min = {min_list}")
if max_list[0] < min_list [0]:
    min_list[0],max_list[0] = max_list[0],min_list[0]
summa=0
for i in range(min_list[0]+1,max_list[0]):
    summa += number_list[i]
print(f"summa = {summa}")
    