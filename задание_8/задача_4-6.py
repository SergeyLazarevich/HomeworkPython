from prettytable import PrettyTable


class OfficeEquipment:
    """Родительский класс описывающий оргтехнику."""
    
    def __init__(self,types,company,year,state,location) -> None:
        self.equipment = {"Тип": types,
                    "Фирма производитель": company,
                    "Год выпуска": year,
                    "Состояние": state,
                    "Место хранения": location
                    }
    
    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"],self.equipment["Фирма производитель"],
                    self.equipment["Год выпуска"],self.equipment["Состояние"],
                    self.equipment["Место хранения"]]
                    )
        return table.get_string()

    def __getitem__(self,key):
        """Перегрузка метода извлечения элемента по индексу

        Args:
            key ([str]): [ключ списка]

        Returns:
            [type]: [значение списка]
        """
        return self.equipment.get(key)

    def keys(self):
        """Метод возвращает список ключей

        Returns:
            [list]: [список ключей]
        """
        return list(self.equipment.keys())


class Printer(OfficeEquipment):
    """Класс наследник от OfficeEquipment описывающий Принтер"""

    def __init__(self, types, company, year, state, location,print_speed) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость печати ст/мин"] = print_speed

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"],self.equipment["Фирма производитель"],
                    self.equipment["Год выпуска"],self.equipment["Состояние"],
                    self.equipment["Место хранения"],self.equipment["Скорость печати ст/мин"]]
                    )
        return table.get_string()

    def __getitem__(self,key):
        """Перегрузка метода извлечения элемента по индексу

        Args:
            key ([str]): [ключ списка]

        Returns:
            [type]: [значение списка]
        """
        return self.equipment.get(key)

    def keys(self):
        """Метод возвращает список ключей

        Returns:
            [list]: [список ключей]
        """
        return list(self.equipment.keys())


class Scanner(OfficeEquipment):
    """Класс наследник от OfficeEquipment описывающий Сканер"""
    
    def __init__(self, types, company, year, state, location,scanner_size) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость сканирования ст/мин"] = scanner_size

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"],self.equipment["Фирма производитель"],
                    self.equipment["Год выпуска"],self.equipment["Состояние"],
                    self.equipment["Место хранения"],self.equipment["Скорость сканирования ст/мин"]]
                    )
        return table.get_string()
    def __getitem__(self,key):
        """Перегрузка метода извлечения элемента по индексу

        Args:
            key ([str]): [ключ списка]

        Returns:
            [type]: [значение списка]
        """
        return self.equipment.get(key)

    def keys(self):
        """Метод возвращает список ключей

        Returns:
            [list]: [список ключей]
        """
        return list(self.equipment.keys())


class XeroxMachine(OfficeEquipment):
    """Класс наследник от OfficeEquipment описывающий ксерокс"""

    def __init__(self, types, company, year, state, location,print_speed,scanner_size) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость печати ст/мин"] = print_speed
        self.equipment["Скорость сканирования ст/мин"] = scanner_size
    
    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"],self.equipment["Фирма производитель"],
                    self.equipment["Год выпуска"],self.equipment["Состояние"],
                    self.equipment["Место хранения"],self.equipment["Скорость печати ст/мин"],
                    self.equipment["Скорость сканирования ст/мин"]]
                    )
        return table.get_string()

    def __getitem__(self,key):
        """Перегрузка метода извлечения элемента по индексу

        Args:
            key ([str]): [ключ списка]

        Returns:
            [type]: [значение списка]
        """
        return self.equipment.get(key)

    def keys(self):
        """Метод возвращает список ключей

        Returns:
            [list]: [список ключей]
        """
        return list(self.equipment.keys())
        

class WarehouseEquipment:
    """Класс описывающий склад."""
    def __init__(self) -> None:
        self.warehouse = {"Принтер": [],
                        "Сканер":  [],
                        "Ксерокс": []
                        }

    def set_equipment(self, types, company, year, state, location,print_speed,scanner_size):
        """Метод который отвечает за приём оргтехники на склад.
            Вместо отсутствующих параметров ставьте – None

        Args:
            types ([types]): [Тип]
            company ([types]): [Фирма производитель]
            year ([types]): [Год выпуска]
            state ([types]): [Состояние]
            location ([types]): [Место хранения]
            print_speed ([types]): [Скорость сканирования ст/мин]
            scanner_size ([types]): [Скорость печати ст/мин]
        """
        try:
            self.set_validation(types, state, location,print_speed,scanner_size)
            if  types == "Принтер":
                self.warehouse["Принтер"].append(Printer(types, company, year, state, location,print_speed))
            elif types == "Сканер":
                self.warehouse["Сканер"].append(Scanner(types, company, year, state, location,scanner_size))
            elif types == "Ксерокс": 
                self.warehouse["Ксерокс"].append(XeroxMachine(types, company, year, state, location,print_speed,scanner_size))
        except TypeError as err:
            print (f" Ошибка: {err}")

    def get_equipment(self,types,position):
        """Метод который отвечает за передачу в определённое подразделение компании.

        Args:
            position ([type]): [Позиция в списке]
        """
        try:
            self.get_validation(types, position)
            if  types == "Принтер":
                return self.warehouse["Принтер"].pop(position)
            elif types == "Сканер":
                return self.warehouse["Сканер"].pop(position)
            elif types == "Ксерокс": 
                return self.warehouse["Ксерокс"].pop(position)
        except TypeError as err:
            print (f" Ошибка: {err}")

    def __str__(self) -> str:
        table = PrettyTable()
        table.add_column("Тип",list(self.warehouse.keys()))
        table.add_column("Количество", [len(self.warehouse["Принтер"]),len(self.warehouse["Сканер"]),len(self.warehouse["Ксерокс"])])
        return f" На складе: \n {table.get_string()}"

    def set_validation(self, types, state, location,print_speed,scanner_size):
        """Метод который отвечает за проверку вводимых данных. 
        Если находит ошибку в данных, генерирует ошибку "TypeError"

        Args:
            types ([types]): [Тип]
            company ([types]): [Фирма производитель]
            year ([types]): [Год выпуска]
            state ([types]): [Состояние]
            location ([types]): [Место хранения]
            print_speed ([types]): [Скорость сканирования ст/мин]
            scanner_size ([types]): [Скорость печати ст/мин]
        """
        types = types.capitalize()
        if types not in  list(self.warehouse.keys()):
            raise TypeError ("Вам не на этот склад, это склад Оргтехники")
        types = types.capitalize()
        if state != "Исправен":
            raise TypeError (f" Сначала {types} отнесите в мастерскую")
        if not isinstance(print_speed, int) or not isinstance(scanner_size, int):
            raise TypeError ("Скорость печати или сканирования должны выражаться целым числом")
        for i in self.warehouse.values():
            for j in i:
                if j["Место хранения"] == location:
                    raise TypeError ("Это место уже занято")
    
    def get_validation(self, types, position):
        """Метод который отвечает за проверку вводимых данных. 
        Если находит ошибку в данных, генерирует ошибку "TypeError"

        Args:
            types ([types]): [Тип]
            position ([int]): [Позиция в списке]
        """
        types = types.capitalize()
        if types not in  list(self.warehouse.keys()):
            raise TypeError ("Вам не на этот склад, это склад Оргтехники")
        if not isinstance(position, int):
            raise TypeError ("Позиция должна выражаться целым числом")
        namber=0
        for i in self.warehouse.values():
            namber += len(i)
        if position>namber:
            raise TypeError ("Такой позиции нет на складе")

    def print_product_range(self):
        """Распечатать весь ассортимент склада"""
        table = PrettyTable()
        cap = self.warehouse["Ксерокс"][0].keys()
        cap.insert(0," № ")
        table.field_names = cap
        # table.field_names = self.warehouse["Ксерокс"][0].keys()
        namber=1
        for i in self.warehouse.values():
            for j in i:
                table.add_row([namber,j["Тип"],j["Фирма производитель"],j["Год выпуска"],j["Состояние"],
                            j["Место хранения"],j["Скорость печати ст/мин"],j["Скорость сканирования ст/мин"]])
                namber+=1
        print(table)




if __name__ in "__main__":
    warehouse = WarehouseEquipment()
    print("Принимаем на склад: \n")
    warehouse.set_equipment("Принтер","Samsung",2020,"Не Исправен", "2-б", 1000, 0)
    warehouse.set_equipment("Сканер","Samsung",2015,"Исправен", "3-a", 0, 20)
    warehouse.set_equipment("Ксерокс","Xserox",2021,"Исправен", "5-г", 1500, 35)
    warehouse.set_equipment("Принтер","Samsung",2020,"Исправен", "1-a", 1000, 0)
    warehouse.set_equipment("Сканер","Samsung",2015,"Исправен", "2-a", 0, 20)
    warehouse.set_equipment("Ксерокс","Xserox",2021,"Исправен", "3-г", "1500", 35)
    warehouse.set_equipment("Принтер","Samsung",2020,"Исправен", "4-б", 1000, 0)
    warehouse.set_equipment("Сканер","Samsung",2015,"Исправен", "2-a", 0, 20)
    warehouse.set_equipment("Ксерокс","Xserox",2021,"Исправен", "4-г", 1500, 35)
    warehouse.set_equipment("Принтер","Samsung",2020,"Исправен", "5-б", 1000, 0)
    warehouse.set_equipment("Монитор","Samsung",2015,"Исправен", "7-a", 0, 20)
    warehouse.set_equipment("Ксерокс","Xserox",2021,"Исправен", "1-г", 1500, "35")
    print("\n Распечатаем всё что есть: \n")
    print(warehouse)
    warehouse.print_product_range()
    print("\n Передадим в другое подразделение компании: \n")
    print(warehouse.get_equipment("Принтер",0))
    print(warehouse.get_equipment("Сканер",0))
    print(warehouse.get_equipment("Ксерокс",0))
    print("\n Распечатаем что осталось: \n")
    print(warehouse)
    warehouse.print_product_range()
