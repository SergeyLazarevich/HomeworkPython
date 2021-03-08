"""
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Zerodivision(Exception):
    """Класс проверки деления на ноль"""

    @staticmethod
    def division(divisor, divisible)-> float:
        """[Функция деления divisor на divisible]

        Args:
            divisor ([float]): [divisor]
            divisible ([float]): [divisible]

        Returns:
            float: [result]
        """
        try:
            return divisor/divisible
        except Exception as err:
            print (f"Ошибка: {err}")
            return None



if __name__ in "__main__":
    namber=[[4.5, 5],[150, 25.3],[6, 0],["4.5", 2],[10, "5"],[25, 5]]
    for i in namber:
        print(f"Деление {i[0]} на {i[1]} = {Zerodivision.division(i[0],i[1])}")
    
