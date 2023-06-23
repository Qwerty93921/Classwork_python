my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]

my_list1.append(6)
print(my_list1)


my_list1.extend(my_list2)
print(my_list1)


my_list1.insert(4, "торт")
print(my_list1)


# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]        
# [1, 2, 3, 4, 'торт', 5, 6, 6, 7, 8, 9, 10]



# append(item) - добавление нового элемента в конец списка

# extend(list) - добавляет элеметы из списка в конец другого списка

# insert(item) - вставляет элемент по указанному индексу