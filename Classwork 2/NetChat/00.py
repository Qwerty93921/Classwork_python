from red import *

class Person():
    __first_name =  ""
    __last_name = ""
    # Подчеркивание означает что НЕЛЬЗЯ МЕНЯТЬ данные

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @red
    def show_info(self):
        print(self.__first_name, self.__last_name)

Amir = Person("Amir", "Yusupov")

# Amir.first_name = "Vasya"
# Не будут меняться данные если захотят их изменить

# print(Amir.first_name, Amir.last_name)

Amir.show_info()
