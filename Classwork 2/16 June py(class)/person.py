from random import randint

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
