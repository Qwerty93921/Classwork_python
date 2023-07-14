my_file = open("input_2.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

words_list = text.split()
print(words_list)

glasnye = "аоуэыяёеюи"
soglasnye = "бвгджзйклмнпрстфхцчшщ"

# for i in range(len(words_list) - 1):
#     print(words_list[i], words_list[i + 1])

b = []

# for i in range(len(words_list)):
#     if words_list[i[i]] == soglasnye and words_list[i[i + 1]] == glasnye:
#         print([i], "-", [i + 1])

for i in range(len(words_list)):
    print(i, words_list[i])
    for i in range(len(words_list[i][i])):
        words_list[i][i].split()
        i = i + 1
    print(words_list[i][i].split())
