import json

# data = '{"type": "forecast", "duration": 3, "city": "Караганда", "country_code": "kz"}'

# request = json.loads(data)
# request["city"] = "Алматы"
# # loads - из строки в словарь


# data = json.dumps(request, ensure_ascii=False)

# # dumps - из словаря(файла) в строку
# ensure_ascii=True ИЗНАЧАЛЬНО, поэтому надо ставить False

# print(data)

with open("14 July text 1.txt", encoding="utf-8") as myfile:
    request = json.load(myfile)

request["city"] = "Алматы"

with open("14 July text 1.txt", "w", encoding="utf-8") as myfile:
    json.dump(request, myfile, ensure_ascii=False)

# Результат что в блокноте изменилось слово "Караганда" на "Алматы"

# print(request["city"])

# dumps - со строками
# dump - с файлами
# json - Java script o... n...
