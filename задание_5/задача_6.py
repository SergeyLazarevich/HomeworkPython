def sum_list(_sum_list_):
    """
    Функция вычисляет сумму чисел в списке из строк "_sum_list_"
    """
    i=None
    j=None
    summa=0
    for strings in _sum_list_:
        for ii in range(len(strings)):
            if not strings[ii].isalpha():
                if i==None:
                    i=ii
                j=ii
            else:
                break
        if j>i:
            summa+=int(strings[i:j])
    return summa


try:
    with open("My_file_6.txt",'r',encoding="UTF-8") as obj_f:
        subject_dist={}
        for strings in obj_f:
            strings=strings.split()
            subject_dist[strings[0][:-1]]=sum_list(strings[1:])
        print(subject_dist)
except IOError as err:
    print(err)