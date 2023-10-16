import re

pattern = r'([A-Za-z]+) (\d+)'
text = "June 24, September 20, October 10"

matched = re.search(pattern, text)

if matched:
    print("Группа 0", matched.group(0))
    print("Группа 1", matched.group(1))
    print("Группа 2", matched.group(2))

# Группа 0 June 24
# Группа 1 June
# Группа 2 24

# ---------------------------------------------------------------------------------------------------------

# re.match(pattern, string) - проверяет начинается ли строка с заданного шаблона
# re.search(pattern, string) - ищет первое совпадение с шаблоном в строке
# re.findall(pattern, string) - ищет все совпадения с шаблоном в строке и возвращает их в виде списка
# re.findfilter(pattern, string) - ...

# d - цифра
# D - не цифра
# w - буква
# W - не буква
