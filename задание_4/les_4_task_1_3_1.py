"""4. Определить, какое число в массиве встречается чаще всего."""

from random import randint

number_list = [randint(0,5) for i in range(20)]
print(number_list)
counter = [0,0]
while number_list:
    number = number_list[0]
    counters = 0
    number_list1  = number_list [0:]
    for i in number_list:
        if i == number:
            counters +=1
            number_list1.remove(number)
    number_list = number_list1 [0:]
    if counter[0] < counters:
        counter[0] = counters
        counter[1] = number
print(counter)

