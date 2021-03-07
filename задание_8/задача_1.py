import datetime


class Dates:
    """Класс Дата"""
    date=0
    manth=0
    year=0

    def __init__(self,text) -> None:
        """функция-конструктор которого принимает дату в виде строки формата «день-месяц-год»

        Args:
            text ([str]): [строки формата «день-месяц-год»]
        """
        text=text.split("-")
        try:
            Dates.date=int(text[0])
            Dates.manth=int(text[1])
            Dates.year=int(text[2])
        except Exception as err:
            print(f"Дата введена не в формате «день-месяц-год». Ошибка: {err}")

    def __str__(self) -> str:
        try:
            return Dates.datatext().strftime("%d:%m:%Y")
        except Exception as err:
            return (f"Ошибка: {err}")

    @staticmethod
    def validating_numbe(dates,manth,year)-> datetime:
        """[Функция проводит валидацию числа,месяца и года]

        Args:
            dates ([int]): [число]
            manth ([int]): [месяц]
            year ([int]): [год]

        Returns:
            datetime: [Класс datetime]
        """
        try:
            dates=datetime.date(year, manth, dates)
            return dates 
        except ValueError as err:
            print(f"Ошибка: {err}")
            return None
    
    @classmethod
    def datatext(cls):
        """[Функция извлекает число, месяц, год и преобразовывает их тип к типу «Число».]"""
        return Dates.validating_numbe(cls.date,cls.manth,cls.year)


if __name__ in "__main__":
    date_run=Dates("27-3-2021")
    print(date_run)


