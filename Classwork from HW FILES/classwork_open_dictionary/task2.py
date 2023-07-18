# Напишите программу, которая читает из файла текст, и выводит на экран только те слова,
# которые являются палиндромами.
# Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево.
my_file = open("palyndromes.txt", encoding="utf-8")
text = my_file.read()
my_file.close()
print(text)

# def ispalyndrome(word):
#     return word == "".join(reversed(word))
#
# result = filter(ispalyndrome, text.split())
# a = ", ".join(result)

text = filter(lambda x: x == x[::-1], text.split())
text = ", ".join(text)
print(text)

