# Сортировка "пузырьком"

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

is_sorted = False
while not is_sorted:
    is_sorted = True
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            is_sorted = False

print(my_list)
