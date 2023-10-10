import re
# regular expresions
# помогает найти совпадения в словах

pattern = r"a...e"

text = "I have an agere"
matched = re.search(pattern, text)
if matched:
    print("Найдено совпадение: ", matched.group())

# re.match(pattern, string) - проверяет начинается ли строка с заданного шаблона
# re.search(pattern, string) - ищет первое совпадение с шаблоном в строке
# re.findall(pattern, string) - ищет все совпадения с шаблоном в строке и возвращает их в виде списка
# re.findfilter(pattern, string) - ...

# d - цифра
# D - не цифра
# w - буква
# W - не буква
