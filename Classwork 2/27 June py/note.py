my_list = [6, 65, 7, 52, 54, 54, 54, 0]

for x in my_list:
    x += 1 # не получится изменить элементы
    pass

for i in range(len(my_list)):
    # 0 1 2 3 4 5 6 7
    my_list[i] += 1 # Элементы изменятся
    pass
