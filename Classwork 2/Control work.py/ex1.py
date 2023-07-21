# Функция возвращает результат деления большего по модулю числа на меньшее.
def smart_div(num1, num2 = None):
    if num2 == None:
        result = num1 / num1
        print(result)
    elif abs(num1) >= abs(num2):
        result = num1 / num2
        print(result)
    elif abs(num2) >= abs(num1):
        result = num2 / num1
        print(result)
    return result

def test_smart_div():
    assert smart_div(20, 4) ==  5
    assert smart_div(3, -6) == -2
    assert smart_div(-8)    ==  1
    
test_smart_div()
