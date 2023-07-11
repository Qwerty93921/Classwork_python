# map, filter, reduce
from functools import reduce



def sum1(a, b):
    return a + b


sum2 = lambda a, b: a + b
print(sum2(2, 3))

print(sum1(2, 3))


# map - соответствие
names = ["Евгений", "Даниил", "Руслан", "Артем", "Ансар", "Шолпан", "Глеб", "Виталий"]

def first_char(text):
    return text[0]

# chars = map(first_char, names)
# print(list(chars))
# # ['Е', 'Д', 'Р', 'А', 'А', 'Ш', 'Г', 'В']



# chars = map(first_char, names)
# for x in chars:
#     print(x)

# Е
# Д
# Р
# А
# А
# Ш
# Г
# В


# names[2] = "_"
# print(list(chars))
# []


# chars = map(lambda x: x[0], names)
# print(list(chars))
# # ['Е', 'Д', 'Р', 'А', 'А', 'Ш', 'Г', 'В']



# big_names = filter(lambda x: len(x) > 6, names)
# print(big_names.__next__())
# print(big_names.__next__())

# Евгений
# Виталий


# ------------------------------------------------------------------------

# REDUCE -----------------------------------------------------------------

result = reduce(lambda acc, x: acc + x, names)
print(result)

# ЕвгенийДаниилРусланАртемАнсарШолпанГлебВиталий

chars = reduce(lambda acc, x: acc + [x[0]] , names, [])
print(chars)

# ['Е', 'Д', 'Р', 'А', 'А', 'Ш', 'Г', 'В']


big_names = reduce(lambda acc, x : acc + [x] if len(x) > 5 else acc, names, [])

print(big_names)

# ['Евгений', 'Даниил', 'Руслан', 'Шолпан', 'Виталий']


