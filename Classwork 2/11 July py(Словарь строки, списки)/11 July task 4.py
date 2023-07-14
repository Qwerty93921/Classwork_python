my_file = open("TEXT_4 July 11.txt", encoding = "utf-8")
text = my_file.read()
my_file.close()

my_list = text.split()
print(my_list)

for element in text:
    print(text.count("a"))





# for i in range(len(my_list)):
#     print(i, end=" ")
#     # if len(element) > 1:
#     #     print(element[0:1])
#     # else:
#     #     break

# Все что в кавычках считается за 1 индекс
