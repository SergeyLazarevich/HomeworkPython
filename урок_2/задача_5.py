my_list = [7, 5, 3, 3, 2]
number=int(input("Введите число: "))
for i in range(0,len(my_list)):
    if number>my_list[i]:
        my_list.insert(i,number)
        break
    if (i+1)==len(my_list):
        my_list.append(number)
print(my_list)
