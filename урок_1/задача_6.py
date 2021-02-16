start=float(input("Введите начальный результат спортсмена:  "))
finish=float(input("Введите конечный результат спортсмена:  "))
days=1
print(f"{days}-й день: {start:.3f}")
while start<finish:
    start=start+start*0.1
    days+=1
    print(f"{days}-й день: {start:.3f}")
print(f"Ответ: на {days}-й день спортсмен достиг результата — не менее {finish} км.")  
