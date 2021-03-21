"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения."""


from random import randint

number_list = [randint(-20,20) for i in range(20)]
print(number_list)
max_min = -20
for i in number_list:
    if i < 0 and i > max_min:
        max_min = i
print(max_min)