from random import randint

# randint - из диапозона

my_list = []

for i in range(10):
    number = randint(-100, 100)
    my_list.append(number)

print(my_list)
