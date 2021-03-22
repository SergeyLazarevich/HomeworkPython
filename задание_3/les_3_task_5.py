"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения."""


from random import randint

number_list = [randint(-20,20) for i in range(20)]
print(number_list)
max_min = [0,-20]
for i in range(len(number_list)) :
    if number_list[i] < 0 and number_list[i] > max_min[1]:
        max_min[0] = i
        max_min[1] = number_list[i]
print(max_min)