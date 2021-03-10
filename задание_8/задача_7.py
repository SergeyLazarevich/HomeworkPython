"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""

class ComplexNumber:
    """Класс  «Комплексное число»"""

    def __init__(self,reals,imaginary) -> None:
        """Класс  «Комплексное число»

        Args:
            reals ([str, int, fload]): [действительные числа]
            imaginary ([str, int, fload]): [действительные числа]
        """
        try:
            self.reals = float(reals)
            self.imaginary = float(imaginary)
        except ValueError as err:
            print (f" Ошибка: {err}")
            self.reals = 0
            self.imaginary = 0

    def __add__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(self,obj_complex)
            return ComplexNumber(self.reals + obj_complex.reals,self.imaginary + obj_complex.imaginary)
        except TypeError as err:
            print (f" Ошибка: {err}")
        
    def __radd__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex,self)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __sub__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(self,obj_complex)
            return ComplexNumber(self.reals - obj_complex.reals,self.imaginary - obj_complex.imaginary)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __rsub__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex,self)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __mul__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(self,obj_complex)
            a = self.reals*obj_complex.reals - self.imaginary*obj_complex.imaginary
            b = self.reals*obj_complex.imaginary + obj_complex.reals*self.imaginary
            return ComplexNumber(a,b)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __rmul__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex,self)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __truediv__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(self,obj_complex)
            a = (self.reals*obj_complex.reals + obj_complex.imaginary*self.imaginary)/(obj_complex.reals**2 + obj_complex.imaginary**2)
            b = (obj_complex.reals*self.imaginary - self.reals*obj_complex.imaginary)/(obj_complex.reals**2 + obj_complex.imaginary**2)
            return ComplexNumber(a,b)
        except TypeError as err:
            print (f" Ошибка: {err}")
    
    def __rtruediv__(self,obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex,self)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __str__(self) -> str:
        if self.imaginary<0:
            return f"{self.reals:.02f} - j*{abs(self.imaginary):.02f}"
        return f"{self.reals:.02f} + j*{self.imaginary:.02f}"

    @staticmethod
    def checking_object_type(object_1,object_2):
        """[Функция проверки типов объектов на равенство]

        Args:
            object_1 ([type]): 
            object_2 ([type]): 

        Raises:
            TypeError: [description]
        """
        if not isinstance(object_2, type(object_1)):
            raise TypeError (f"Тип объекта {type(object_1)} не равен {type(object_2)}")

if __name__ in "__main__":
    z1=ComplexNumber(-2,6)
    z2=ComplexNumber(5,-9)
    print(z1)
    print(z2)
    print(f"({z1}) + ({z2}) = {z1+z2}")
    print(f"({z1}) - ({z2}) = {z1-z2}")
    print(f"({z2}) - ({z1}) = {z2-z1}")
    print(f"({z1}) * ({z2}) = {z1*z2}")
    print(f"({z2}) / ({z1}) = {z2/z1}")
    print(f"({z1}) / ({z2}) = {z1/z2}")
    z1=ComplexNumber("-2",6)
    z2=ComplexNumber(5,"-9")
    print(z1)
    print(z2)
    z4=ComplexNumber("-2","y")
    print(z4)
    z3=ComplexNumber("f",-9)
    print(z3)
    print(f"(b) + ({z1}) = {'b'+z1}")
    print(f"({z1}) - 1 = {z1-1}")
    print(f"({z2}) - 1.5 = {z2-1.5}")
    print(f"(b) * ({z1}) = {'b'*z1}")
    print(f"2 / ({z2}) = {2/z2}")
    print(f"({z1}) / 5.3 = {z1/5.3}")