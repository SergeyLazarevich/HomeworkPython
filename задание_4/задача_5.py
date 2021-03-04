from functools import reduce

def my_func (prev_el, el):
    """
    prev_el - предыдущий элемент
    el - текущий элемент

    Функция произведения двух элементов
    """
    return prev_el * el

#Создаём список из чётных чисел от 100 до 1000 (включая границы).
original_list=[i for i in range(100,1001) if i%2==0]
print(f"Чётные чисела от 100 до 1000: {original_list}")
print(f"Произведение всех элементов списка = {reduce(my_func, original_list)}")
