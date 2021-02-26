class Stationery:
    """
    Родительский класс для рисования
    """
    def __init__(self) -> None:
        self.title="пальцем"
    def draw(self)->None:
        """
        Метод для отображения рисунка 
        """
        print(f"Рисуем {self.title}")

class Pen(Stationery):
    """
    Класс карандаш
    """
    def __init__(self) -> None:
        self.title="ручкой"

class Pencil(Stationery):
    """
    Класс ручка
    """
    def __init__(self) -> None:
        self.title="карандашом"

class Handle(Stationery):
    """
    Класс маркер
    """
    def __init__(self) -> None:
        self.title="маркером"

finger=Stationery()
pen=Pen()
pencil=Pencil()
handle=Handle()
finger.draw()
pen.draw()
pencil.draw()
handle.draw()

