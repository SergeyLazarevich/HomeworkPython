from sys import argv


def salary(hourly_rate:str, hour:str, premium:str) -> str:
    """
    Функция получает параметры зарплаты работника, производит расчёт,
    и возвращает зароботную плату работника 
    """
    return str(( float(hourly_rate)* float(hour))+ float(premium))


script_name,hourly_rate, hour, premium = argv
print(f"расчёт заработной платы сотрудника: {salary(hourly_rate, hour, premium)}")
