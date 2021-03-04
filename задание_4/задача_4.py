from random import randint
#Создаём список
original_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#Выводим на печать
print("Исходный список")
print(original_list)
#Создаём новый список из элементов исходного списка не имеющие повторений.
generated_list=[i for i in original_list if original_list.count(i)==1]
#Выводим на печать
print("Полученный список ")
print(generated_list)
#Сгенерируем список с псевдослучайными целыми числами  
original_list=[randint(0,20) for i in range(20)]
#Выводим на печать
print("Сгенерируем список из 20 элементов с псевдослучайными целыми числами от 0 до 20")
print(original_list)
#Создаём новый список из элементов исходного списка не имеющие повторений.
generated_list=[i for i in original_list if original_list.count(i)==1]
#Выводим на печать
print("Полученный список ")
print(generated_list)
