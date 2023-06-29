# Вывести каждый 4-й элемент из указанного пользователем диапазона
user_begin = input("Введите начало диапазона: ")
user_end   = input("Введите конец диапазона: ")
try:
    begin = int(user_begin)
    end = int(user_end)
except ValueError:
    begin = end = None


if begin is None or end is None:
    print("Нужны целые числа!")
else:
    x = begin
    while x < end:
        x += 4
        print(x)



