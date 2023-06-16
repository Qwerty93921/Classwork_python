from random import randint
# Можно import random


class Person:
    balance = 0
    name = ""
    iin = 0
    age = 0
    ticket = None



    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.iin = randint(100000000000, 999999999999)   # self.iin = random.random


    def show(self):
        message = " Человек %s, возраст %s, ИИН: %s. Денег: %s" %(self.name, self.age, self.iin, self.balance)
        print(message)


    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance < amount:
            return 0
        self.balance -= amount
        return amount


class Ticket:
    number = 0
    passenger_name = ""
    passenger_iin = 0
    passenger_age = 0
    source = ""
    destination = ""

    def __init__(self, source, destination, pas_name, pas_iin, pas_age):
        self.number = randint(100000, 999999)
        self.source = source
        self.destination = destination
        self.passenger_name = pas_name
        self.passenger_iin = pas_iin
        self.passenger_age = pas_age

    def show(self):
        message = "Билет №%s: %s -- %s " % (self.number, self.source, self.destination)
        message += "Пассажир: %s, %s лет, ИИН: %s" % (self.passenger_name, self.passenger_age, self.passenger_iin)
        print(message)


class Kassa:
    balance = 0

    def get_price(self, source, destination):
        return(len(source) + len(destination)) * 1000

    def buy_ticket(self, source, destination, person):
        money = person.pay(self.get_price(source, destination) )
        if money:
            self.balance += money
            person.ticket = Ticket(source, destination, person.name, person.iin, person.age)
        else:
            print("No money = no ticket!111!!!1111!!!11")


class Train:
    source = ""
    destination = ""
    number = 0

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.number = randint(10000, 99999)

    def board(self, person):
        if person.ticket:
            if self.source == person.ticket.source and self.destination == person.ticket.destination:
                message = "Добро пожаловать %s, ваш поезд №%s прибыл, от %s до %s." % (person.name, self.number, self.source, self.destination)
                print(message)
                person.ticket = None
            else:
                print("Неправильный билет")
        else:
            print("Нет билета")       

    def show(self):
        message = "Поезд №%s, от станции %s до станции %s." % (self.number, self.source, self.destination)
        print(message)




test_man = Person("Elon Musk", 55)
test_man.earn(30000)
test_man.pay(13000)
test_man.show()

# test_ticket = Ticket("Алматы", "Сантьяго", test_man.name, test_man.iin, test_man.age)
# test_ticket.show()

kassa = Kassa()
price = kassa.get_price("Алматы", "Сантьяго")
kassa.buy_ticket("Алматы", "Сантьянго", test_man)


if test_man.ticket:
    test_man.ticket.show()

train = Train("Алматы", "Сантьянго")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("Билета больше нет")
