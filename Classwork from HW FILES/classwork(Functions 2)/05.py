import random
def get_random_int(min, max):
    result = random.random() * (max - min)
    result += min
    return int(result)


def game(my_random, min, max):
    user_in = input("Угадай число от %s до %s: " % (min, max))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Только целое число вводи!")
        game(my_random, min, max)
    else:
        if my_random > user_num:
            print("Больше ;)")
            game(my_random, min, max)
        elif my_random < user_num:
            print("Меньше :)")
            game(my_random, min, max)
        else:
            print("Правильно, %d!" % my_random)
            return

num = get_random_int(0, 20)
game(num, 0, 20)

