# Минимальные числа выводит в НОВЫЙ список

user_in = input("Введите числа через запятую:")

user_in = user_in.split(",")

my_list = [int(i) for i in user_in]

sorted_list = []

# for i in range(len(my_list)):
#     min_elem = min(my_list)
#     sorted_list.append(min_elem)
#     del my_list[my_list.index(min_elem)]

# print(sorted_list)

# Введите числа через запятую:6,3,8,1,9,4 
# [1, 3, 4, 6, 8, 9]

for i in range(len(my_list)):
    min_index = 0
    for k in range(1, len(my_list)):
        if my_list[k] < my_list[min_index]:
            min_index = k
    
    sorted_list.append(my_list[min_index])
    del my_list[min_index]

print(sorted_list)
