my_file = open("book.txt", encoding="utf-8")

text = my_file.read()
my_file.close()

user_input_1 = input("Введите текст который вы хотите заменить: ")
user_input_2 = input("Введите текст на который вы хотите  его заменить: ")

a = text.replace(user_input_1.lower(), user_input_2.lower())
a = a.replace(user_input_1.upper(), user_input_2.upper())
a = a.replace(user_input_1.capitalize(), user_input_2.capitalize())

print(a)

# Введите текст который вы хотите заменить: миссис
# Введите текст на который вы хотите  его заменить: ЫВЫФВЫВФЫВФФВЫЫВФЫФВФВЫ
