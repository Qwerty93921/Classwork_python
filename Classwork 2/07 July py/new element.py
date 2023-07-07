fruits = {"apple": 1, "banana": 2, "orange": 3}

fruits["banana"] = 4 # Измение значения
# fruits["kiwi"] = 5 # Добавление нового элемента

new_key = "kiwi"
fruits[new_key] = 5

print(fruits)

# {'apple': 1, 'banana': 4, 'orange': 3, 'kiwi': 5}