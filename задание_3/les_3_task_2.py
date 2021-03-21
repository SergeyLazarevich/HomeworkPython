"""2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив 
надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), 
т. к. именно в этих позициях первого массива стоят четные числа."""

from random import randint


number_list = [randint(1,2) for i in range(20)]
print(number_list)
exit_list=[]
for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        exit_list.append(i)
print(exit_list)
