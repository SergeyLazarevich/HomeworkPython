class Road:
    """
    Класс производит расчёт массы асфальта, требуемого для
    покрытия дороги шириной "length", длинной "width" и толщиной "depth"
    """
    def __init__(self, length:int, width:int, depth:int)->None:
        self.__length = length
        self.__width = width
        self.__mass = 5
        self.__depth = depth

    def mass_calculation(self)->None:
        """
        Метод расчёт массы асфальта
        """
        massa=(self.__length*self.__width*(self.__mass*self.__depth)*self.__depth)/1000
        print(f"Масса асфальта, необходимого для покрытия всей дороги = {massa:.2f} т.")


Mass_Road=Road(20,5000,5)
Mass_Road.mass_calculation()