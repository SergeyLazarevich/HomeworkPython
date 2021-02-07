number=int(input("Введите целое положительное число: "))
max=0
intermediate_variable=number
while intermediate_variable>0:
    if (intermediate_variable%10)>max:
        max=(intermediate_variable%10)
    intermediate_variable=intermediate_variable//10
print(f"Cамая большая цифра в числе {number} равна {max}")
