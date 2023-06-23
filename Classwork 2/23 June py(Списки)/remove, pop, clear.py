my_list_1 = [1, 2, 5, True, "cake"]
element_removed = my_list_1.remove("cake")

print(my_list_1, element_removed)

# -------------------------------------------------------------

element_popped = my_list_1.pop(3)  # True - 3 элемент, возвращает его

print(my_list_1, element_popped)

# -------------------------------------------------------------

my_list_1.clear()
print(my_list_1)

# [1, 2, 5, True] None
# [1, 2, 5] True
# []




# remove(item) - удаляет элемент из списка

# pop(index) - возвращает элемент по указанному индексу и удаляет его из списка

# clear() - удаляет все элементы из списка
