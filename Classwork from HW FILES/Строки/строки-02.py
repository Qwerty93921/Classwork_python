string  = input("Введите строку: ")
user_in = input("Сколько раз повторить? ")
repeats = int(user_in)

result = string * repeats
template = "Результат: %s"
message = template % result

print(message[3:])