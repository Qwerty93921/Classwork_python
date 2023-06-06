import random

def get_random_int(min, max):
    result = random.random() * (max - min)
    result = result + min
    return int(result)


num = get_random_int(10, 20)
print(num)
