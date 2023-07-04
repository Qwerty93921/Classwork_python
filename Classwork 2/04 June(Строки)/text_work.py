my_file = open("book.txt", encoding="utf-8")

# text = my_file.read() # читает как большую строку
text = my_file.readlines() # Каждую строку делает списком и читает ОТДЕЛЬНО
my_file.close()

print(text)

# new_text = text.replace("миссис", "WORD12345")

# print(new_text)
