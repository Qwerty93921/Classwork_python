class Car:

    def __init__(self, model, speed, color, bak_max, consumption):
        self.model = model
        self.speed = speed
        self.color = color
        self.bak_max = bak_max
        self.consumption = consumption / 100 # литров на 1 км(на 100 по стандарту)
        self.fuel_volume = 5 # константа - 5 литров в новой машине
        # consumption - потребление

    def refuel(self, litres):
        if self.fuel_volume + litres <= self.bak_max:
            self.fuel_volume += litres
            print("В баке: ", self.fuel_volume, "литров")
        else:
            over_fill = self.fuel_volume + litres - self.bak_max
            # перелив - слишком много бензина и бак ПОЛНЫЙ и остальное ВЫЛИВАЕТСЯ 
            self.fuel_volume = self.bak_max
            print("Перелив, бак полный, в вашем баке %d литров" % over_fill )

    def go(self, km):
        fuel_waste = self.consumption * km # потребление топлива за киллометр
        if self.fuel_volume >= fuel_waste:
            time = km / self.speed
            self.fuel_volume -= fuel_waste
            print("Мы приехали за %s часов и в баке осталось %d литров" % (time, self.fuel_volume))
            # %.2f - 2 знака после запятой
        else:
            print("На поездку надо %d литров, в баке сейчас %d" % (fuel_waste, self.fuel_volume))


class PorsheCayenne(Car):
    
    def __init__(self, color):
        super().__init__("PorsheCayenne", 150, color, 60, 10)


my_car = PorsheCayenne("black")
my_car.go(80)
my_car.refuel(30)
my_car.go(10)
