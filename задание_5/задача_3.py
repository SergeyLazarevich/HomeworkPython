try:
    with open("My_file_3.txt",'r',encoding="UTF-8") as obj_f:
        sum=0
        i=0
        for line in obj_f:
            if float(line.split()[1])<20000.00:
                print(line,end="")
            sum+=float(line.split()[1])
            i+=1
        print(f"Средняя величина дохода сотрудников: = {sum/i:.2f}")
except IOError as err:
    print(err)