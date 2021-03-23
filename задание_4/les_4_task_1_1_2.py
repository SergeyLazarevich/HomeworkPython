from cProfile import run

def test(func):
    lst = [[4,3,2,1,1,1,1,1],[49,33,24,19,16,14,12,11],
            [499,333,249,199,166,142,124,111],
            [4999,3333,2499,1999,1666,1428,1249,1111],
            [49999,33333,24999,19999,16666,14285,12499,11111],
            [499999,333333,249999,199999,166666,142857,124999,111111]]
    for i, item in enumerate(lst):
        assert item == func(10**(i+1))
        print(f"Test {i+1}  OK")

"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов."""

def func(n):
    list_nuber = [0]*8
    for i in range(2,10):
        for j in range(2,n):
            if  j % i == 0:
                list_nuber[i - 2] +=1
    return list_nuber


# test(func)

# run("func(1000)")
# 4 function calls in 0.004 seconds
# 1    0.003    0.003    0.003    0.003 les_4_task_1_1_1.py:16(func)

# run("func(1000000)")
# 4 function calls in 3.451 seconds
# 1    3.450    3.450    3.450    3.450 les_4_task_1_1_2.py:16(func)

# "les_4_task_1_1_2.func(10)"
# 1000 loops, best of 5: 9.05 usec per loop

# "les_4_task_1_1_2.func(100)"
# 1000 loops, best of 5: 68.1 usec per loop  

# "les_4_task_1_1_2.func(1000)"
# 1000 loops, best of 5: 733 usec per loop

# "les_4_task_1_1_2.func(10000)"
# 1000 loops, best of 5: 7.84 msec per loop

