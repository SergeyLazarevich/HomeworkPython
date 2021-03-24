"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре 
квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для 
всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и 
ниже среднего."""

from collections import OrderedDict

list_enterprises = OrderedDict()
qty = int(input("Введите количество предприятий: "))
summa = 0
for i in range(qty):
    strt = input("Введите наименованиe: ")
    a = []
    a.append(int(input("Введите прибыль за четыре квартала: ")))
    list_enterprises[strt] = a
    summa += a[0]
summa = summa / qty
list_enterprises["Средняя прибыль: "] = summa
print(f"Средняя прибыль: {summa}")
for i,item in enumerate(list_enterprises.items()):
    if i == len(list_enterprises) - 1 :break
    list_enterprises[item[0]].append(item[1][0] - summa)
    print(f"{item[0]} отклонение от средней прибыли {item[1][0] - summa}")


