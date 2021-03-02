"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix ():
    """
    класс Matrix

    """
    def __init__(self, matrix_list: list):
        """
        Args:
            matrix_list (list): [description]
        """
        self.matrix_list = matrix_list

    def __str__(self) -> str:
        matrix_str="\n"
        for i in self.matrix_list:
            for j in i:
                matrix_str=f"{matrix_str}{j}   "
            matrix_str=f"{matrix_str}\n"
        return matrix_str
    
    def __add__(self, obj_matrix):
        try:
            if type(obj_matrix)!=Matrix:
                raise Exception('В функцию передан объект не типа "Matrix"')
            if len(self.matrix_list)!=len(obj_matrix.matrix_list):
                raise Exception("Количество строк матрици А не равно количеству строк матрицы Б")
            else:
                for i in range(len(obj_matrix.matrix_list)):
                    if len(self.matrix_list[i])!=len(obj_matrix.matrix_list[i]):
                        raise Exception("Количество столцов матрици А не равно количеству столбцов матрицы Б")
            add_matriks=[[0] * len(self.matrix_list[i]) for i in range(len(self.matrix_list))]
            for i in range(len(self.matrix_list)):
                for j in range(len(self.matrix_list[i])):
                    add_matriks[i][j]=self.matrix_list[i][j]+obj_matrix.matrix_list[i][j]
            return Matrix(add_matriks)
        except Exception as err:
            print(err) 
        




matrix_list=Matrix([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
matrix_list_1=Matrix([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
matrix_list_2=matrix_list+matrix_list_1
if type(matrix_list_2)==Matrix:
    print(f"{matrix_list}\n     +\n{matrix_list_1}\n     =\n{matrix_list_2}")