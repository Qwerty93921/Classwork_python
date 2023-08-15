# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    my_str = ("")
    new_phrase = phrase.split()
    for i in new_phrase:
        letter = i[0:1].upper()
        my_str += letter
    print(my_str)
    return my_str


def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''

test_get_abbr()
