list_tovar=[]
nuber=0
while True:
    nuber+=1
    list_cotalog={"название":" ", "цена": 0.0, "количество": 0, "eд": "шт."}
    list_nuber=(nuber,list_cotalog)
    list_tovar.append(list_nuber)
    list_cotalog["название"]=input("Введите название товара: ")
    list_cotalog["цена"]=float(input("Введите цену товара: "))
    list_cotalog["количество"]=int(input("Введите количество товара: "))
    if input("продолжить да/нет:  ")=="да":
        continue
    else:
        break
print(list_tovar)
list_analiz={"название": [],"цена": [],"количество": [],"ед": "шт."}
for i in range(0,len(list_tovar)):
    list_analiz["название"].append(list_tovar[i][1]["название"])
    list_analiz["цена"].append(list_tovar[i][1]["цена"])
    list_analiz["количество"].append(list_tovar[i][1]["количество"])
print(f"название: {list_analiz['название']}")
print(f"цена: {list_analiz['цена']}")
print(f"количество: {list_analiz['количество']}")
print(f"ед: {list_analiz['ед']}")
