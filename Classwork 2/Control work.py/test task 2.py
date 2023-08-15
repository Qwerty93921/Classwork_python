stroka = "семь раз отмерь - один раз отрежь"
new_stroka = stroka.split()
print(new_stroka)

# for i in range(len(new_stroka)):
#     print(i, stroka[i][0:1])

for i in new_stroka:
    print(i[0:1].upper(), end="")
