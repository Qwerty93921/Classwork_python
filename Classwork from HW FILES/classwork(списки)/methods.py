first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9]

first_list.append(6)
print(first_list)

first_list.extend(second_list)
print(first_list)

first_list.insert(4, "торт")
print(first_list)
###############################

third_list = [1, 2, 5, True, "cake", "ololo"]
element_removed = third_list.remove("cake")
print(third_list, element_removed)

element_popped = third_list.pop(3)
print(third_list, element_popped)

third_list.clear()
print(third_list)
###############################


first_list = [1, 2, 5, True, "cake", "ololo"]
something = "ololo"
my_index = first_list.index(something)
print(my_index)  # 5

###############################

first_list = [1, "cake", 2, 5, False, "cake", "ololo", "cake"]
total = first_list.count("cake")
print(first_list)
print("Total -", total)

###############################

third_list = ["slovo", "nut", "mars", "olovo", "yetti"]
result = third_list.sort(reverse=True)

print(third_list)
print(result)

###############################

forth_list = ["Hello", 666, 0, "sun", [8, 7, 6]]
forth_list.reverse()
print(forth_list)

fifth_list = forth_list.copy()
# fifth_list = forth_list
fifth_list[2] = "welcome"
fifth_list[0][2] = "A"

print(fifth_list)
print(forth_list)

print(fifth_list is forth_list)