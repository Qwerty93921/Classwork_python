# Свойста и методы есть в ООП

class Kettle():
    material = "steel"
    color = "red"
    volume = 2.4

my_kettle = Kettle()
other_kettle = Kettle()
my_kettle.color = "blue"

Kettle.color = "white"

print( my_kettle.material )

