string_list=(input("Введите строку из нескольких слов: ").rstrip(" ")).split(" ")
for i in range(0,len(string_list)):
    string_list[i]=f"{i+1}. {string_list[i]}"
    print((string_list[i])[:13])