user_input1 = int(input("Введите первое число: "))
number_1 = user_input1

user_input2 = int(input("Введите второе число: "))
number_2 = user_input2

if number_1 > number_2:
    print("Наименьшее число это число номер 2 =", number_2)

elif number_1 < number_2:
    print("Наименьшее число это число номер 1 =",number_1)

else:
    print("Числа равны")
