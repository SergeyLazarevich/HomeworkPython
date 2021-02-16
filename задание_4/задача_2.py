from random import shuffle
#Исходный список
print("Исходный список")
original_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#Выводим на печать
print(original_list)
#Создаём новый список из элементов исходного списка значения которых больше предыдущего элемента
generated_list=[original_list[i] for i in range(1,len(original_list)) if original_list[i]>original_list[i-1]]
#Выводим на печать
print("Полученный список ")
print(generated_list)
#Перемешивает элементы исходного списка  
shuffle(original_list)
#Выводим на печать
print("Перемешивает элементы исходного списка ")
print(original_list)
#Создаём новый список из элементов исходного списка значения которых больше предыдущего элемента
generated_list=[original_list[i] for i in range(1,len(original_list)) if original_list[i]>original_list[i-1]]
#Выводим на печать
print("Полученный список ")
print(generated_list)
