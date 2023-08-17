class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.__floors = floors
        self.__color = color
        self.__rooms = rooms
        self.__bathrooms = bathrooms

    def get_info(self):
        info = "Дом %d-этажный, цвета %s, комнат: %d, ванных: %d" % \
                (self.__floors, self.__color, self.__rooms, self.__bathrooms)
        return info

    def change_color(self, new_color):
        if new_color:
            self.__color = new_color


class HouseWithBalcony(House):
    def __init__(self, floors, color, rooms, bathrooms, balconys):
        super().__init__(floors, color, rooms, bathrooms)
        self.__balconys = balconys

    def get_info(self):
        info = super().get_info()
        return info + f", балконов: {self.__balconys}"



my_house = HouseWithBalcony(2, "красный", 6, 2, 2)
my_house.change_color("зелёный")
info = my_house.get_info()
print(info)
