# 1

user_input = input("Введите числа через запятую: ")
user_list = user_input.split(",")

# 2

# numbers = []

# for x in user_list:
#     numbers.append(int(x))

# print(user_list)
# print(numbers)

# 3

def get_last_digit(num):
    return num % 10        # Остаток от деления на 10

print(user_list)

list_length = len(user_list)

try:

    for i in range(list_length):
        user_list[i] = int(user_list[i])

except ValueError:
    message = "Нужны только числа и через запятую"

else:
    end_list = sorted(user_list, key=get_last_digit, reverse=True) # По убыванию
    another_list = [str(x) for x in end_list]
    message = " - ".join(another_list)

print(message)



# 8234,230,21,45,29532
# 45, 8234, 29532, 21, 230 ----------------------  0.5, 0.4, 0.2, 0.1, 0 - остатки ПОСЛЕ деления на 10 в обратном порядке
# Сверху остатки ПОСЛЕ деления на 10 в ОТВЕТЕ 



# В обратном порядке(по убыванию) выстраивает числа - ОСТАТОК после ДЕЛЕНИЯ на 10
