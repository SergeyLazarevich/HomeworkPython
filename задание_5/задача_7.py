import json


final_list=[]
try:
    with open("My_file_7.txt",'r',encoding="UTF-8") as obj_f:
        profit={}
        average_profit={}
        summa=0
        i=0
        for le in obj_f:
            le=le.split()
            profit[le[0]]=(int(le[2])-int(le[3][:-1]))
            if profit[le[0]]>0:
                summa+=profit[le[0]]
                i+=1
        average_profit['average_profit']=round(summa/i,2)
        final_list=[profit,average_profit]
except IOError as err:
    print(err)

try:
    with open("My_file_7_7.txt",'w',encoding="UTF-8") as obj_f:
        json.dump(final_list,obj_f)
except IOError as err:
    print(err)