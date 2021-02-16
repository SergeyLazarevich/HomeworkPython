from itertools import cycle

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
