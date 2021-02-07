seconds=int(input("Введите количество секунд: "))
minutes=0
hours=0
if seconds>=3600:
    hours=seconds//3600
    seconds=seconds-hours*3600
if seconds>=60:
    minutes=seconds//60
    seconds=seconds-minutes*60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
