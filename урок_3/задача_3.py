def max_sum(namber_1,namber_2,namber_3):
    """
    функция принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов
    """
    fun_list=[namber_1,namber_2,namber_3]
    fun_min=min(fun_list)
    fun_list.remove(fun_min)
    return sum(fun_list)


my_namber_1=int(input("Введите первое число: "))
my_namber_2=int(input("Введите второе число: "))
my_namber_3=int(input("Введите третье число: "))
print(f"Сумма наибольших двух аргументов = {max_sum(my_namber_1,my_namber_2,my_namber_3)}")
