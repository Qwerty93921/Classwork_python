user_input = int(input("Введите цену на продукт: "))
cost = user_input
#1500

if cost < 1000:
    print("Скидок нет")
elif cost < 2000:
    print("Скидка 2%")
elif cost < 5000:
    print("Скидка 5%")
else:
    print("Скидка 10%")

print("Конец")

