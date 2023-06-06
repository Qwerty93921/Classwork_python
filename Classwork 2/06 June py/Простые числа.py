def is_simple(num, divider = 2):
    if num < 2:
        return False
    if divider >= num:
        return True
    if num % divider == 0:
        return False
    else:
        return is_simple(num, divider + 1)





print(1, is_simple(1) )
print(5, is_simple(5) )
print(29, is_simple(29) )
