def division(namber_1,namber_2):
    """
    namber_1/ namber_2

    функция получает два аргумента и производит деление namber_1 на namber_2,
    дополнительно проверяет условие деления на ноль 
    """
    try:
        return namber_1/namber_2
    except ZeroDivisionError:
        return "на ноль делить нельзя"


my_namber_1=float(input("введите делимое: "))
my_namber_2=float(input("введите делитель: "))
print(f"{my_namber_1}/{my_namber_2}={division(my_namber_1,my_namber_2)}")
