from random import randint

my_list = []

first_random = randint(-100, 100)
second_random = randint(-100, 100)
print(first_random, second_random)

# Диапозон от двух чисел

for i in range(10):
    if first_random > second_random:
        number = randint(second_random, first_random)
        my_list.append(number)
    else:
        number = randint(first_random, second_random)
        my_list.append(number)

print(my_list)
