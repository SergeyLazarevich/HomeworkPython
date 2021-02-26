class Car:
    """
    Базовый класс автомобиля
    speed – скорость
    color – цвет
    name – марка
    is_police – флаг полицейского автомобиля
    """
    def __init__(self,speed: int, color: str, name: str) -> None:
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=False
        self.direction="прямо"
        self.go_stop=False
    
    def go(self):
        """
        Метод сообщает о начале движения автомобиля
        """
        self.go_stop=True
        print(f"Машина {self.color} {self.name} поехала")
    
    def stop(self):
        """
        Метод сообщает об остановке автомобиля
        """
        self.go_stop=False
        self.speed=0
        print(f"Машина остановилась")

    def turn(self,direction="прямо"):
        """
        Метод сообщает о повороте автомобиля
        """
        self.direction=direction
        if self.direction=="прямо":
            print(f"Машина едет {self.direction}")
        else:
            print(f"Машина повернула на {self.direction}")
    
    def show_speed(self):
        """
        Метод сообщает о движении автомобиля
        """
        if not self.go_stop:
            print("Мы стоим")
            return
        print(f"Машина едет со скоростью {self.speed} км/час")
        if self.is_police:
            print(f"Полицейский автомобиль включи МИГАЛКУ ВСЕ ПРИЖАЛИСЬ К ОБОЧИНЕ!!!!")


class TownCar(Car):
    """
    Класс электромобиля
    """
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)
        self.speed_limit=60

    def show_speed(self):
        """
        Метод сообщает о движении автомобиля
        """
        super().show_speed()
        if self.speed>self.speed_limit:
            print(f"Вы превышаете скорость заданную для данного автомобиля на {self.speed-self.speed_limit} км/час")


class SportCar(Car):
    """
    Класс спорткара
    """


class WorkCar(Car):
    """
    Класс рабочего автомобиля
    """
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)
        self.speed_limit=40

    def show_speed(self):
        """
        Метод сообщает о движении автомобиля
        """
        super().show_speed()
        if self.speed>self.speed_limit:
            print(f"Вы превышаете скорость заданную для данного автомобиля на {self.speed-self.speed_limit} км/час")


class PoliceCar(Car):
    """
    Класс полицейского автомобиля
    """
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)
        self.is_police=True


def new_func1(TownCar, SportCar, WorkCar, PoliceCar):
    car_1=TownCar(65,"красный","Audi")
    car_2=SportCar(120,"синий","Bugatti")
    car_3=WorkCar(80,"зелёный","Daewoo")
    car_4=PoliceCar(90,"радужный","Ford")
    return car_1,car_2,car_3,car_4


def new_func(car):
    car.go()
    car.show_speed()
    car.turn()
    car.turn("лево")
    car.turn("право")
    car.stop()
    car.show_speed()


car_1, car_2, car_3, car_4 = new_func1(TownCar, SportCar, WorkCar, PoliceCar)
new_func(car_1)
new_func(car_2)
new_func(car_3)
new_func(car_4)
