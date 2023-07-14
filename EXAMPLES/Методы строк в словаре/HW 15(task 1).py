my_file = open("input.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

changed_text = text.split()

# print(changed_text)
# ['Example@mail.ru', 'Word', '120', 'apple', 'Johnson@gmail.com', 'Alex456@mail.eu']

mail_list = []

for i in range(len(changed_text)):
    if "@" in changed_text[i]:
        mail_list.append(changed_text[i])
    else:
        continue

print("Список почт:\n" ,mail_list)



second_file = open("output.txt", "w", encoding="utf-8")

for i in range(len(changed_text)):
    if "@" in changed_text[i]:
        mail_list.append(changed_text[i])
        second_file.write(mail_list[i] + "\n")
    else:
        continue

second_file.close()
