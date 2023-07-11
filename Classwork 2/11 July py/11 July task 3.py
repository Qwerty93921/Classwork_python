my_file = open("TEXT_3 July 11.txt", encoding = "utf-8")
text = my_file.read()
my_file.close()

print(text)

text = text.split()
print(text)

numbers_in_word = 0


for element in text:
    if element.isdigit() == False:
        continue
    else:
        print("Цифр в тексте:", len(element))
