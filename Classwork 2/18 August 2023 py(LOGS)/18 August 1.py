# *nums - это создание списка и можно вводить сколько угодно аргументов

def my_sum(*nums):
    result = 0
    for x in nums:
        result += x
    return result

print(my_sum(5, 8, 8, 43, 3, 100))
# 167
