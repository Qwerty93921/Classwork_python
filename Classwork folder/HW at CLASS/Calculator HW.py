user_input1 = float(input("Введите первое число: "))
user_input2 = float(input("Введите второе число: "))


template = """
Сумма чисел:        %.2f
Разность чисел:     %.2f
Произведение чисел: %.2f
Частное чисел:      %.2f
"""

try:
    num1 = float(user_input1)
    num2 = float(user_input2)

except ValueError:
    message = "Вы ввели неправильные данные"

else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    message = template % (sum, sub, mul, div)

print(message)

# %.2f - это 2 знака после запятой(дробное число)
# Template - шаблон

