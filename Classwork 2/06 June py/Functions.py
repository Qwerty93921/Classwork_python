# def имя функции (список аргументов):
#     тело
#     функции


# def my_function(x, y=0):
#     тело функции
# my_function(3)


def factor(num):    # factor - придуманное название
    if num == 1:    
        return 1    # Если число 1 то возвращается 1
    return num * factor(num - 1)    # Если 2, тогда 2 * (2 -1) = 2


result = factor(6)
print(result)

# Рекурсия
