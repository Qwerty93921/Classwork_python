a = [43, 65, 3, 43, 6]

# Обход по значениям
# for i in a:
#     print(i, index(i))

# Обход по индексам
# МОЖНО МЕНЯТЬ ЗНАЧЕНИЯ В СПИСКЕ!!!!!!


# for i in range(len(a)):
#     print(i, a[i])


# 0 43
# 1 65
# 2 3
# 3 43
# 4 6

# for i in range(5) = for i in range(0, 5) = ОТ 0 ДО 4
# ----------------------------------------------------------------------------------------------------------------

for i in range(len(a)):
    print(i, a[i])
    a[i] += 5

print(a)

# 0 43
# 1 65
# 2 3
# 3 43
# 4 6
# [48, 70, 8, 48, 11]

# В списке ИЗМЕНИЛИСЬ значения