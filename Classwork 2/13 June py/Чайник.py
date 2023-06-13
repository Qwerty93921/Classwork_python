class Kettle():
    temperature = 20
    material = ""
    color = ""
    volume = 0
    water = 0

    def __init__ (self, material, volume, color = None):
        self.material = material
        self.volume = volume
        if color is not None:
            self.color = color

    def fill(self, liters): # fill налить
        self.water += liters
        if self.water > self.volume:
            extra = self.water - self.volume
            print(f"Пролилось {extra} л лишней воды")
            self.water = self.volume
        print(f"Теперь в чайнике {self.water} л")


    def pour(self, liters): #pour вылить
        if liters > self.water:
            print(f"Не могу вылить больше чем {self.water} л")
            self.water = 0
        else:
            self.water -= liters
        print(f"Теперь в чайнике {self.water} л")



    def boil(self):
        self.temperature = 100
        print("СВИСТ!!!!!!!!!!!!!!!!!!!!!!!")





my_kettle = Kettle("bamboo", 5, "yellow")
my_kettle.fill(3)

Kettle.color = "black"

other_kettle = Kettle("Iron", 0.7)
print(other_kettle.color)


other_kettle.fill(3.5)
other_kettle.boil()
other_kettle.pour(4)
