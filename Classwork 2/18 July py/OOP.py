class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.__floors = floors
        self.color = color
        self.__rooms = rooms
        self.__bathrooms = bathrooms
        # В свои свойства добавляет это
        # __init__ - он инициализирует данные, это КОНСТРУКТОР
    
    def get_info(self):
        info = "Дом %d-этажный, цвета: %s, комнат: %d, ванных: %d" % \
                (self.__floors, self.color, self.__rooms, self.__bathrooms)
        return info

    # \ означает продолжение строки
    # __rooms = нельзя менять данные из-за ДВУХ ПОДЧЕРКИВАНИЙ

    def change_color(self, new_color):
        if new_color:
            self.__color = new_color

    # Если что то есть в color, тогда выполняется функция 
    # Есои пусто тогда нет


class HouseWithBalcony(House):   # связывается с другим классом В СКОБКАХ
    def __init__(self, floors, color, rooms, bathrooms, balconys):
        super().__init__(floors, color, rooms, bathrooms)
        self.__balconys = balconys

    def get_info(self):
        info = super().get_info()
        return info + f", балконов: {self.__balconys}"


my_house = HouseWithBalcony(2, "красный", 6, 2, 2)
my_house.color = "зеленый"
my_house.__rooms = 22
my_house.__floors = 17
# Изменение свойств класса

info = (my_house.get_info())
print(info)


# Дом 2-этажный, цвета: зеленый, комнат: 6, ванных: 2, балконов: 2
# ИЗМЕНЕН ТОЛЬКО ЦВЕТ



# Дом 2-этажный, цвета красный, комнат: 6, ванных: 2
# super - связывается С КЛАССОМ

# Наследование - копирует все от родителя
# Полиморфизм - Возможность изменить родительские методы(чтобы у дочерних элементов свойства были изменены)
# Инкапсуляция - некоторые свойства и методы внутри классов можно СКРЫТЬ(что-то можно изменить и нельзя)
