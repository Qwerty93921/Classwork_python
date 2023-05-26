string = input("Введите строку: ")
user_input = input("Сколько раз повторить? ")
repeats = int(user_input)

result = string * repeats
template = "Результат: %s"
#template = шаблон

message = template % result

print(message)
