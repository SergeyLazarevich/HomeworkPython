from itertools import cycle
from time import sleep


class TrafficLight:
    """
    Класс TrafficLight описывает работу светофора, 
    и проверяет последовательность переключения цветов
    """
    __colors={"Красный":7,"Желтый":2,"Зелёный":5}
    __check={"Красный":"Зелёный","Желтый":"Красный","Зелёный":"Желтый"}
    
    def running(self)-> None:
        """
        Метод описывает работу светофора, 
        и проверяет последовательность переключения цветов
        """
        i=0
        check_color="Зелёный"
        for key in cycle(self.__colors):
            i+=1
            if i>9:break
            if check_color != self.__check[key]:
                print("ВНИМАНИЕ на программу светофор произведена хакерская атака, программа прекращает свою работу!!!!")
                break
            else:
                check_color=key
                print(f'Цвет светофора "{key}" через {self.__colors[key]} секунд он изменится')
                sleep(self.__colors[key])

    def hak(self)-> None:
        """
        Метод имитирует хакерскую атаку
        """
        self.__colors={"Зелёный":7,"Зелёный":2,"Зелёный":5}


traffic_light=TrafficLight()
traffic_light.running()
traffic_light.hak()
traffic_light.running()
