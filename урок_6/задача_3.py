class Worker:
    """
    Класс формирует анкету работника
        name - имя работника
        surname - фамилия работника
        position - должность работника
        wage - оклад работника
        bonus - премия работника
    """
    def __init__(self,name:str,surname:str,position:str,wage: int, bonus: int) -> None:
        self.name=name
        self.surname=surname
        self.position=position
        self.__income={"wage":wage,"bonus":bonus}

class Position(Worker):
    """
    Класс реализует методы вывода информации о работнике
    """
    def __init__(self,name:str,surname:str,position:str,wage:int, bonus:int) -> None:
        super().__init__(name,surname,position,wage, bonus) 

    def get_full_name(self)->None:
        """
        Метод получения полного имени сотрудника
        """
        print(f"Имя работника: {self.name}")
        print(f"Фамилия работника: {self.surname}")

    def get_total_income(self):
        """
        Метод получения дохода с учётом премии
        """
        print(f"Доход с учётом премии = {self._Worker__income['wage']+self._Worker__income['bonus']}")


worker_1=Position("Ivan","Ivanov","worker",100, 20)
worker_2=Position("Petr","Petrov","worker",120,40)
worker_2.get_full_name()
worker_2.get_total_income()
worker_1.get_full_name()
worker_1.get_total_income()