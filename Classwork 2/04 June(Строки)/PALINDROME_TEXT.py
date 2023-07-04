my_file = open("palindrome.txt", encoding="utf-8")

text = my_file.read()
my_file.close()


def is_palindrome(word):
    return word == "".join(reversed(word))


result = filter(is_palindrome, text.split())
print(list(result))

# ['казак', 'и', 'мем', 'шалаш', 'тут', 'казак', 'око', 'и', 'А']