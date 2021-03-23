from cProfile import run

def test(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    for i, item in enumerate(lst):
        assert item == func(i+1)
        print(f"Test {i+1}  OK")


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
    m=n*30
    lst=[2]
    for i in range(3, m+1, 2):
        if len(lst) == n: break
        if (i > 10) and (i%10==5):continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):break
        else:
            lst.append(i)
    return lst[-1]

# print(prime(1))

# test(prime)

# run("prime(100)")
# 374 function calls in 0.001 seconds
#  0.001    0.001    0.001    0.001 les_4_task_2_2.py:19(prime)

# run("prime(10000)")
# 62368 function calls in 1.079 seconds
# 1    1.042    1.042    1.079    1.079 les_4_task_2_2.py:19(prime)

# "les_4_task_2_2.prime(100)"
# 1000 loops, best of 5: 218 usec per loop

# "les_4_task_2_2.prime(500)"
# 1000 loops, best of 5: 2.12 msec per loop

# "les_4_task_2_2.prime(1000)"
# 1000 loops, best of 5: 5.51 msec per loop