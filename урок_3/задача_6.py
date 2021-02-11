def fun_title(string):
    """
    Функция принимает слова из маленьких латинских букв и
    возвращающую их же, но с прописной первой буквой.
    """
    return string.title()

my_string=input("Вветите слова из маленьких латинских букв: ")
print(fun_title(my_string))