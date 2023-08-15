# Сортировка "пузырьком"
# По 2 элемента рассматривает друг с другом, тот что меньше выводит назад(первее в списке), затем сравнивает другие 2 числа и так до конца

user_in = input("Введите числа через запятую:")

user_in = user_in.split(",")

# my_list = list(map(lambda x: int(x), user_in))
# Перевод в int формат

my_list = [int(i) for i in user_in]
# Перевод в int формат

is_sorted = False

while not is_sorted:
    is_sorted = True
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            is_sorted = False

print(my_list)

# Введите числа через запятую:74,5,9,6,2,0,1
# [0, 1, 2, 5, 6, 9, 74]
