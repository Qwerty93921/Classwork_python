user_input = input("Введите ваш возраст: ")

try:
    user_age = int(user_input)
except ValueError:
    user_age = ""

if type(user_age) is int:
    if 0 < user_age < 120:
        message = "Ваш возраст реальный"
    else:
        message = "Ваш возраст ненастоящий"

else:
    message = "Вы ввели не число"

print(message)
