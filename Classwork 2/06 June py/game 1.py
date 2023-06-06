import random

def get_random_int(min, max):
    result = random.random() * (max - min)
    result = result + min
    return int(result)

def game():
    user_input = input("Угадай число от 0 до 100: ")
    try:
        user_num = int(user_input)
    except ValueError:
        print("Только целое число введи")
        game()
    else:
        if my_random > user_num:
            print("Больше :)")
            game()
        elif my_random < user_num:
            print("Меньше :)")
            game()
        elif my_random == user_num:
            print("Вы угадали, %d!" % my_random)
            return


my_random = get_random_int(0, 100)
game()
