def sum_list(_sum_list_):
    """
    Функция вычисляет сумму чисел в списке из строк "_sum_list_"
    """
    summa=0
    for i in _sum_list_:
        try:
            summa+=float(i)
        except ValueError as err: 
            print("Error ", err) 
            continue
    return summa


try:
    with open("My_file_5.txt",'w',encoding="UTF-8") as obj_f:
        print(input("Введите набор чисел, разделённых пробелами: "), file=obj_f)
except IOError as err:
    print(err)

try:
    with open("My_file_5.txt",'r',encoding="UTF-8") as obj_f:
        le=obj_f.readline().split()
        print(f"Cумма чисел = {sum_list(le)}")
except IOError as err:
    print(err)