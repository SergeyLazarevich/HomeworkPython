with open("My_file_1.txt",'a',encoding="UTF-8") as obj_f:
    while True:
        string_info=input("Введите информацию для записи в файл: ")
        if string_info:
            print(string_info,file=obj_f)
        else:
            break