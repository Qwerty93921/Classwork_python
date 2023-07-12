vowels = "aeiou"
s = "aertiooikjoaikl"
n = len(s)
# vowels = гласные

for i in range(n - 1):
    if s[i] in vowels and s[i + 1] in vowels:
        print(s[i], s[i + 1])

# a e
# i o
# o o
# o i
# o a
# a i

# -1 потому что у самого КРАЙНЕГО СПРАВА элемента НЕТ СОСЕДА СПРАВА, поэтому -1
# ПОПАРНО выводит буквы
