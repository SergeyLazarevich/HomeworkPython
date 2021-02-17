def my_func_1(x, y):
    """
    возведение в степень с помощью оператора **
    """
    return x**y


def my_func_2(x, y):
    """
    возведение в степень с помощью цикла
    """
    rez=1
    if y<0:
        y=abs(y)
        for i in range(0,y):
            rez*=x
        return 1/rez
    else:
        for i in range(0,y):
            rez*=x
        return rez


while True:
    try:
        namber=float(input("Введите действительное положительное число x = "))
    except ValueError as err: 
        print("Error ", err) 
        continue
    if namber>=0:
        break
    else:
        continue
while True:
    try:
        power=int(input("Введите целое отрицательное число y = "))
    except ValueError as err: 
        print("Error ", err) 
        continue
    if power<0:
        break
    else:
        continue
print(f"Первый способ: {my_func_1(namber, power):.10f}")
print(f"Второй способ: {my_func_2(namber, power):.10f}")


