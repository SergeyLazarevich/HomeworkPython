from itertools import count, cycle

def my_fun_count(start=0, stop=10,my_list=[]) ->list:
    """
    start=0 - число — стартового параметра
    stop=20 - количество генерируемых чисел 
    my_list=[] - список сгенерированных чисел 

    Функция генерирующая целые числа, начиная с указанного;
    """
    iter=count(start)
    for i in range(0,stop):
        my_list.append(next(iter))
    return my_list


def my_fun_cycle(my_list=[]) ->list:
    """
    my_list=[] - список сгенерированных чисел 

    Функция повторяющая элементы некоторого списка, определённого заранее;
    """
    iter=cycle(my_list)
    my_list_double=[]
    for i in range(0,len(my_list)):
        my_list_double.append(next(iter))
    return my_list_double
