my_file = open("book.txt", encoding="utf-8")
#text = my_file.read()
text = my_file.readlines()
my_file.close()

print(text)
