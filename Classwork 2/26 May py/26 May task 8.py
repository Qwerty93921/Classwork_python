user_money = int(input("Введите количество денег у вас в кармане: "))
price = int(input("Введите цену шоколадки: "))

try:
    amount_of_chocolate = user_money // price
    money_left = user_money % price
except ValueError:
    print("Вы ввели не число")

print("Ваша сдача: ", money_left,
"Сколько шоколадок вы можете купить: ", amount_of_chocolate)
