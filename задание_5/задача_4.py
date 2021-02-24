try:
    with open("My_file_4.txt",'r',encoding="UTF-8") as obj_f:
        number_dict={"One":"Один","Two":"Два","Three":"Три","Four":"Четыре","Five":"Пять"}
        with open("My_file_4_4.txt",'w',encoding="UTF-8") as f_obj:
            for le in obj_f:
                le=le.split()
                for i in number_dict:
                    if le[0]==i:
                        print(f"{number_dict[i]} {' '.join(le[1:])}",file=f_obj)
except IOError as err:
    print(err)