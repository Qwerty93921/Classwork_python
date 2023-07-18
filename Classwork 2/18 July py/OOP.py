class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.floors = floors
        self.color = color
        self.rooms = rooms
        self.bathrooms = bathrooms
        # В свои свойства добавляет это
        # __init__ - он инициализирует данные, это КОНСТРУКТОР
    
    def get_info(self):
        info = "Дом %d-этажный, цвета %s, комнат: %d, ванных: %d" % \
        (self.floors, self.color, self.rooms, self.bathrooms)
        return info

    # \ означает продолжение строки

my_house = House(2, "красный", 6, 2)
print(my_house.get_info())

# Дом 2-этажный, цвета красный, комнат: 6, ванных: 2
