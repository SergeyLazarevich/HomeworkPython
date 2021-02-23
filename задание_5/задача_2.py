try:
    with open("My_file_1.txt",'r',encoding="UTF-8") as obj_f:
        stroka=0
        slova=0
        for line in obj_f:
            stroka+=1
            slova+=len(line.split(" "))
    print(f"Строк в файле: = {stroka}")
    print(f"Слов в файле: = {slova}")
except IOError as err:
    print(err)