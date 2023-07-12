my_file = open("TEXT_1 July 11.txt", encoding="utf-8")
text = my_file.read()
my_file.close()


if text.startswith("abc"):
    text = text.replace("abc", "www.", 1) # Сколько раз сделать замену
else:
    text.endswith(".com")

print(text)
