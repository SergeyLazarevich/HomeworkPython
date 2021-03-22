"""2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения 
простого числа должна принимать на вход натуральное и возвращать соответствующее простое 
число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте 
этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту."""

def prime(n: int)-> int:
    """[Функция нахождения i-го по счёту простого числа]

    Args:
        n (int): [номер по порядку в таблице простых чисел]

    Returns:
        int: [простое чисело]
    """
    lst=[2]
    for i in range(3, n*10+1, 2):
        if (i > 10) and (i%10==5):continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):break
        else:
            lst.append(i)
        if len(lst) == n: break
    return lst[-1]


n = int(input("n="))
print(prime(n))