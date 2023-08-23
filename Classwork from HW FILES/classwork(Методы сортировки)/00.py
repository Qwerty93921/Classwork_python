
def the_function(the_list, i):
    if 0 <= i < len(the_list):
        return the_list[i]
    return None


def second_func(the_list, i=0):
    for x in the_list:
        i += x
    return i


def third_func(the_list, i=0):
    for x in the_list:
        for y in the_list:
            i += x * y
    return i




a = the_function([54,21,65,67,43,86,43,5,-2], 5)

b = second_func([54,21,65,67,43,86,43,5,-2], 5)
