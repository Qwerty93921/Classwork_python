from functools import reduce

words = ['slovo', 'another', 'geek', 'supernatural']

## Вариант 1
smallest_len = 999999999
for x in words:
    word_len = len(x)
    if word_len < smallest_len:
        smallest_len = word_len  # запоминаем длину

print(smallest_len)

## Вариант 2
def shortest(x, y):
    if len(x) > len(y):
        return y
    else:
        return x

smallest_word = reduce(shortest, words)
print(len(smallest_word))

