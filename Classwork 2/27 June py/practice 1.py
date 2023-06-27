user_input = input("Введите список чисел через запятую:")
user_in = user_input.split(',')
user_list = [int(x) for x in user_in]

for x in range(len(user_list)):
    if user_list[x] % 2:
        user_list[x] -= 3
    else:
        user_list[x] *= 2

print(user_list)

