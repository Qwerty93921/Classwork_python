# Делит список на 3 отдела: МЕНЬШЕ опорного элемента(первое число в списке(pivot)), САМ опорный элемент, затем числа которые БОЛЬШЕ опорного элемента

user_in = input("Введите числа через запятую:")

user_in = user_in.split(",")

my_list = [int(i) for i in user_in]

def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    pivot = the_list[0]
    
    less = list(filter(lambda x: x < pivot, the_list))

    # first_list = [x for x in the_list if x < pivot]

    equals = list(filter(lambda x: x == pivot, the_list))
    more = list(filter(lambda x: x > pivot, the_list))
    result = quick_sort(less) + equals + quick_sort(more)
    return result

print(quick_sort(my_list))

# 2,5,71,3,7,1,2,6,8

# Введите числа через запятую:2,5,71,3,7,1,2,6,8
# [1, 2, 2, 3, 5, 6, 7, 8, 71]
