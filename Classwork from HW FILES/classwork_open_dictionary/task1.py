# Разработайте программу, которая заменяет все вхождения заданного слова в тексте на другое слово.
# Программа читает текст из файла, спрашивает у пользователя старое слово и новое слово, на которое
# нужно заменить. И в тексте заменяются все эти слова, как в нижнем регистре, так и в верхнем.
# Получившийся текст вывести на экран.

my_file = open("book.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

user_in1 =input("Введите текст, который Вы хотите заменмить: ")
user_in2 =input("Введите текст на который Вы хотите его заменмить: ")
a = text.replace(user_in1.lower(), user_in2.lower())
a = a.replace(user_in1.upper(), user_in2.upper())
a = a.replace(user_in1.capitalize(), user_in2.capitalize())
print(a)
