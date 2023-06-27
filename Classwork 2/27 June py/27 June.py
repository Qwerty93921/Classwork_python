class Dog:
    type = ""
    size = 0
    color = ""

    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color

    def bark(self):
        print("Гав-гав!!!!111!!!!111!!")
        print(self.color)

my_little_dog = Dog("foxxterier", 20, "white")
my_little_dog.bark()
