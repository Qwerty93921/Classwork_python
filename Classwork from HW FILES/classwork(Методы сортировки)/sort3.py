# Быстрая сортировка

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    pivot = the_list[0]
    less = list(filter(lambda x:  x < pivot, the_list))
    # less = [x for x in the_list if x < pivot]
    equals = list(filter(lambda x: x == pivot, the_list))
    more = list(filter(lambda x: x > pivot, the_list))
    result = quick_sort(less) + equals + quick_sort(more)
    return result


print(quick_sort(my_list))
