def is_simple(num, div=2):
    if num < 2:
        return False
    if div >= num:
        return True
    if num % div == 0:
        return False
    else:
        return is_simple(num, div+1)


print( is_simple(9.5) )
print(1, is_simple(1) )
print(5, is_simple(5) )
print(29, is_simple(29) )