"""
3. Реализовать программу работы с органическими клетками. 
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, 
    соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
    сложение (__add__()), 
    вычитание (__sub__()), 
    умножение (__mul__()), 
    деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять 
    увеличение, 
    уменьшение, 
    умножение и обычное (не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно 
    равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если 
    разность количества ячеек двух клеток больше нуля, иначе выводить 
    соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки 
    определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется 
    как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр 
    класса и количество ячеек в ряду. Данный метод позволяет организовать 
    ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., 
    где количество ячеек между \n равно переданному аргументу. Если ячеек на 
    формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернет строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
def cheek(fun):
    """Декоратор для функций класса OrganicCell, сравнивающий тип
    передаваемого класса с исходным"""
    def cheek_obj(*args,**kvargs):
        if not isinstance(args[1], type(args[0])):
            raise TypeError(f'В функцию передан объект не типа {type(args[0])}')
        return fun(*args,**kvargs)
    return cheek_obj


class OrganicCell:
    """
    Класс органическая клетка
    """
    valume=5  #количество ячеек в ряду
    def __init__(self,namber: int):
        """
        Инициализация класса органическая клетка
        Args:
            namber (int)
        """
        self.namber=namber

    def __str__(self)->str:
        """
        Метод позволяет организовать ячейки по рядам и возвращает строку вида *****\n*****\n*****
        Returns:
            str: 
        """
        i=self.namber//self.valume
        j=self.namber%self.valume
        lists=[*['*'*self.valume for _ in range(i)], '*'*j]
        return '\n'.join(lists)

    @cheek
    def __add__(self, obj: object)-> object:
        """
        Метод сложения классов OrganicCell
        Args:
            obj (OrganicCell)

        Returns:
            object (OrganicCell)
        """
        return OrganicCell(self.namber+obj.namber)
    
    @cheek
    def __sub__(self,obj)-> object:
        """
        Метод вычитания классов OrganicCell
        Args:
            obj (OrganicCell)

        Returns:
            object (OrganicCell)
        """
        if self.namber<obj.namber:
            raise AssertionError("Разность количества ячеек двух клеток меньше нуля")
        return OrganicCell(self.namber-obj.namber)

    @cheek
    def __mul__(self,obj)-> object:
        """
        Метод умножения классов OrganicCell
        Args:
            obj (OrganicCell)

        Returns:
            object (OrganicCell)
        """
        return OrganicCell(self.namber*obj.namber)

    @cheek
    def __truediv__(self,obj)-> object:
        """
        Метод деления классов OrganicCell
        Args:
            obj (OrganicCell)

        Returns:
            object (OrganicCell)
        """
        if not obj.namber:
            raise ZeroDivisionError("Клетка-делитель пуста")
        return OrganicCell(self.namber//obj.namber)
    
    def make_order(self,volume: int)-> str:
        """
        Метод позволяет организовать ячейки по рядам и возвращает строку вида *****\n*****\n*****
        Args:
            volume (int)
        """
        self.valume=volume
        print(self.__str__())

    
a=OrganicCell(12)
b=OrganicCell(5)
try:
    print(f"Сумма:\n{a+b}")
    print(f"Разность:\n{a-b}")
    print(f"Умножение:\n{a*b}")
    print(f"Деление:\n{a/b}")
    print(f"Замена количества ячеек в ряду:")
    a.make_order(10)
    print(f"Замена количества ячеек в ряду:")
    b.make_order(10)
    print(f"Замена количества ячеек в ряду:")
    (a*b).make_order(10)
except Exception as err:
    print(f'Ошибка: {err}')