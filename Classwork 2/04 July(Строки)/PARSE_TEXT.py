my_file = open("mail.txt", encoding="utf-8")

text = my_file.read()
my_file.close()

def find_email(word):
    for i in range(len(word)):
        if word[i] == "@":
            return True
    else:
        return False

filtered = filter(find_email, text.split())
print(list(filtered))

# ['word123@mail.ru', 'word345@gmail.com']