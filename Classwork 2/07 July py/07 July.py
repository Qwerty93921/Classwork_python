my_file = open("book_2.txt", encoding="utf-8")
text = my_file.read() # Сколько символов читать в скобках (с 1 отсчет)
# my_file.write("\n И тебе привет")
my_file.close()

print(text)
