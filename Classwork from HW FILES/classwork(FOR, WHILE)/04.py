#Вывести все числа от 1 до 100, которые кратные указанному пользователем числу

user_in = input("Введите число: ")
try:
    user_num = int(user_in)
except ValueError:
    user_num = None

if user_num is None:
    print("Нужно целое число!")
else:
    for x in range(1, 100):
        if x % user_num == 0:
            print(x)

