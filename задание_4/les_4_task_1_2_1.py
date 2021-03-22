"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

from random import randint

number_list = [randint(-100,100) for i in range(20)]
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
print(f"max = :{max_list}")
print(f"min = :{min_list}")
min_list[0],max_list[0] = max_list[0],min_list[0]
number_list[max_list[0]] = max_list[1]
number_list[min_list[0]] = min_list[1]
print(f"max = :{max_list}")
print(f"min = :{min_list}")
print(number_list)