def salary(hourly_rate:str, hour:str, premium:str) -> str:
    """
    Функция получает параметры зарплаты работника, производит расчёт,
    и возвращает зароботную плату работника 
    """
    return str((int(hourly_rate)*int(hour))+int(premium))

from sys import argv
script_name,hourly_rate, hour, premium = argv
print(f"расчёт заработной платы сотрудника: {salary(hourly_rate, hour, premium)}")
