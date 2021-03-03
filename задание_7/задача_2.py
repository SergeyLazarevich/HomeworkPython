"""
    Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
3) Реализовать программу работы с органическ
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    """
    Абстрактный класс Одежда
    """
    @abstractmethod
    def calculation_fabric(self):
        """
        Метод рассчитывает расход по формуле для соответствующего типа одежды
        """
        self.name=""
        pass

    @property
    def calculate(self):
        """
        Вывод результата подсчета общего расхода ткани
        """
        return self.calculation_fabric()

    def __str__(self):
        return self.name


class Coat(Clothes):
    """
    Класс Пальто
    """
    def __init__(self, size: int) -> None:
        """
            IN: size - размер палбто
        """
        self.name="Пальто"
        self.size = int(size)

    def calculation_fabric(self):
        return round(self.size/6.5+0.5, 2)


class Suit(Clothes):
    """
    Класс Костюм
    """
    def __init__(self, height: float) -> None:
        """
            IN: height - рост костюма
        """
        self.name="Костюм"
        self.height = float(height)

    def calculation_fabric(self):
        return round(2*self.height+0.3, 2)


size=56
coat = Coat(size)
height=1.73
suit = Suit(height)
print(f"Чтобы изготовить {coat} {size} размера потребуется {coat.calculate} метров квадратных ткани.")
print(f"Чтобы изготовить {suit} {height} роста потребуется {suit.calculate} метров квадратных ткани.")
