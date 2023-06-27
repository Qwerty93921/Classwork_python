fourth_list = ["Hello", 666, 0, "sun"]
fourth_list.reverse()

print(fourth_list)

# -------------------------------------------------------------


fifth_list = fourth_list.copy()
fifth_list[2] = "Bla-bla"

print(fifth_list)
print(fifth_list is fourth_list)
print(fourth_list)

# ['sun', 0, 666, 'Hello']
# ['sun', 0, 'Bla-bla', 'Hello']
# False
# ['sun', 0, 666, 'Hello']

# reverse() - обратный порядок списка

# copy() - возвращает поверхностную копию списка