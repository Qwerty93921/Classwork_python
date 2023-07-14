my_file = open("TEXT_2 July 11.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

print(text)

my_list = text.split()
print(my_list)

len_list = []

for word in my_list:
    word_number = len(word)
    print(word, "=", word_number, "букв")
    len_list.append(word_number)

print(len_list)
print("Самое короткое слово имеет:",min(len_list), "букв")


# Версия препода
# smallest_len = 999999999

# for x in my_list:
#     word_len = len(x)
#     if word_len < smallest_len:
#         print(x) # вроде
