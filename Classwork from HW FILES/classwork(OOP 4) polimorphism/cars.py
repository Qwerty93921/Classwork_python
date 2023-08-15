class Car:
    def __init__(self, model, speed, color, bak_max, consumption):
        self.model = model
        self.speed = speed
        self.color = color
        self.bak_max = bak_max
        self.consumption = consumption / 100
        self.fuel_volume = 5

    def refuel(self, litres):
        if self.fuel_volume + litres <= self.bak_max:
            self.fuel_volume += litres
            print("В баке:", self.fuel_volume, "л")
        else:
            over_fill = self.fuel_volume + litres - self.bak_max
            self.fuel_volume = self.bak_max
            print("Перелив:", over_fill, "л , бак полный")

    def go(self, km):
        fuel_waste = self.consumption * km
        if self.fuel_volume >= fuel_waste:
            time = km / self.speed
            self.fuel_volume -= fuel_waste
            print("Мы приехали за %.2f часов и в баке осталось %s литров" % (time, self.fuel_volume))
        else:
            print("На поезку надо %s л, а в баке всего %s" % (fuel_waste, self.fuel_volume))


class PorsheCayenne(Car):
    def __init__(self, color):
        super().__init__('PorsheCayenne', 150, color, 60, 10)


class Zhiguli(Car):
    def __init__(self, color, extra_light):
        super().__init__("Zhiguli", 100, color, 45, 15)
        self.extra_light = extra_light



my_car = PorsheCayenne("Красный")
my_car.go(80)
my_car.refuel(30)
my_car.go(10)

your_car = Zhiguli("Белый", "Синий")
your_car.refuel(40)
your_car.go(250)
