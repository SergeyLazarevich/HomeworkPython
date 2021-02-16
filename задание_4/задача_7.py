from math import factorial

def fact(stop):
    """
    Функция реализовывает генератор, отвечающий за получение факториала чисел последовательности от 1 до stop
    """
    for i in range(1,stop+1):
        yield factorial(i)


while True:
    try:
        n=int(input("Введите целое неотрицательное число (n) последовательности от 1 до n>=1: "))  
    except ValueError:
        print("Введённый символ не является числом!!!")
        continue
    if n==0:
        print("0!=1")
        break
    elif n<0:
        print("Факториал определён только для целых неотрицательных чисел")
        continue
    else:
        i=1
        for el in fact(n):
            print(f"{i}!={el}", end='; ')
            i+=1
        break
