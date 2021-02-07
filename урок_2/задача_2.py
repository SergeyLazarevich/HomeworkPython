list=[]
index=0
while True:
    list.insert(index,input("Заполните список элементов: ")) 
    index+=1
    if input("продолжить да/нет:  ")=="да":
        continue
    else:
        break
print(list)
for index in range(0,len(list),2):
    if (index+1)!=len(list):
        list[index],list[index+1]=list[index+1],list[index]
print(list)