from my_fun_count import my_fun_count
from my_fun_cycle import my_fun_cycle

print("Генерируем целые числа, начиная с указанного (по умолчанию 10)")
my_list=my_fun_count()
print(my_list)
print("Повторяем элементы списка, определённого заранее")
my_list_double=my_fun_cycle(my_list) 
print(my_list_double)
