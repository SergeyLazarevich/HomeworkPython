def profile(first_name, last_name, year_of_birth, city_of_residence, email, phone):
    """
    first_name - имя
    last_name - фамилия
    year_of_birth - год рождения
    city_of_residence - город проживания
    email - email
    phone - телефон

    Функция которая принимает несколько параметров, описывающих данные
    пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
    Осуществляет вывод данных о пользователе одной строкой.
    """
    print(f"Имя: {first_name}, Фамилия: {last_name}, Год рождения: {year_of_birth}, Город проживания: {city_of_residence},  Email: {email},  Телефон: {phone}")


my_first_name=input("Введите имя: ")
my_last_name=input("Введите фамилию: ")
my_year_of_birth=input("Введите год рождения: ")
my_city_of_residence=input("Введите город проживания: ")
my_email=input("Введите email: ")
my_phone=input("Введите телефон: ")
profile(first_name=my_first_name, last_name=my_last_name, year_of_birth=my_year_of_birth, city_of_residence=my_city_of_residence, email=my_email, phone=my_phone)