def fun_capitalize(string):
    """
    Функция принимает слова из маленьких латинских букв и
    возвращающую их же, но с прописной первой буквой.
    """
    return string.capitalize()

my_string=input("Вветите строку из маленьких латинских букв: ").split(" ")
for i in range(0,len(my_string)):
    my_string[i]=fun_capitalize(my_string[i])
print(" ".join(my_string))
