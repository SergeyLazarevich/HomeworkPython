"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных 
программах в рамках первых трех уроков. Проанализировать результат и определить 
программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить 
в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС 
и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof 
после каждой переменной, а проявили творчество, фантазию и создали универсальный
код для замера памяти."""

import sys

print(f'Версия python: {sys.version}')
print(f'Версия OS: {sys.platform}')

def memory_count(lst):
    """Функция подсчёта оперативной памяти затрачиваемой на переданную переменную"""
    if not hasattr(lst, '__iter__'): return sys.getsizeof(lst)
    memory = 0
    for var in lst:
        spam = sys.getsizeof(var)
        if hasattr(var, '__iter__') and not isinstance(var, str):
            if hasattr(var, 'keys'):
                for key, value in var.items():
                    spam += memory_count([key]) + memory_count([value])
            else:
                spam += memory_count(var)
        memory += spam
    return memory


"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

def func_1(number_list):
    min_list = [0,100]
    max_list = [0,-100]
    for i in range(len(number_list)):
        if number_list[i] > max_list[1]:
            max_list[0] = i
            max_list[1] = number_list[i]
        if number_list[i] < min_list[1]:
            min_list[0] = i
            min_list[1] = number_list[i]
    number_list[max_list[0]] = min_list[1]
    number_list[min_list[0]] = max_list[1]
    print(f"number_list = {memory_count(number_list)}")
    print(f"min_list = {memory_count(min_list)}")
    print(f"max_list = {memory_count(max_list)}")
    return number_list
# Затраты памяти программы:  2856
# Переменные:  number_list = 2748
#              min_list = 52
#              max_list = 56

def func_2(number_list):
    min_list = min(number_list)
    max_list = max(number_list)
    min_pos = number_list.index(min_list)
    max_pos = number_list.index(max_list)
    number_list[min_pos] = max_list
    number_list[max_pos] = min_list
    print(f"number_list = {memory_count(number_list)}")
    print(f"min_list = {memory_count(min_list)}")
    print(f"max_list = {memory_count(max_list)}")
    print(f"min_pos = {memory_count(min_pos)}")
    print(f"max_pos = {memory_count(max_pos)}")
    return number_list
# Затраты памяти программы:  2856
# Переменные:  number_list = 2748
#              min_list = 24
#              max_list = 28
#              min_pos = 28
#              max_pos = 28

def func_3(number_list):
    num_min = number_list[0]
    min_index = 0
    num_max = number_list[0]
    max_index = 0
    for i, item in enumerate(number_list):
        if item < num_min:
            num_min = item
            min_index = i
        elif item > num_max:
            num_max = item
            max_index = i
    number_list[max_index], number_list[min_index] = number_list[min_index], number_list[max_index]
    print(f"number_list = {memory_count(number_list)}")
    print(f"num_min = {memory_count(num_min)}")
    print(f"min_index = {memory_count(min_index)}")
    print(f"num_maxt = {memory_count(num_max)}")
    print(f"max_index = {memory_count(max_index)}")
    return number_list
# Затраты памяти программы:  2856
# Переменные:  number_list = 2748
#              num_min = 24
#              min_index = 28
#              num_maxt = 28
#              max_index = 28

number_list = [4, 0, 2, 1, 4, 4, 1, 0, 3, 2, 5, 0, 5, 4, 5, 0, 4, 3, 1, 4, 1, 3, 5, 4, 1, 3, 4, 5, 2, 3, 4, 0, 3, 5, 4, 2, 5, 5, 5, 4, 3, 2, 3, 1, 2, 0, 5,1, 5, 5, 4, 2, 3, 4, 2, 4, 5, 5, 0, 4, 1, 1, 0, 1, 1, 0, 3, 4, 4, 3, 3, 3, 1, 0, 1, 3, 2, 2, 1, 0, 5, 3, 4, 0, 2, 2, 4, 0, 5, 1, 3, 2, 2, 1, 5, 3, 3, 2, 5, 1]
func_1(number_list)
func_2(number_list)
func_3(number_list)

# ********************************************************************************************************
# Версия python: 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)]
# Версия OS: win32

# ВЫВОД: Использование дополнительных переменных занимает в памяти больше места, но их наличие порой облегчает
# читабельность кода. Сччитаю, что хорошим компромиссом этих критериев будет вариант 2, если учитовать
# тесты на скорость выполнения программы 