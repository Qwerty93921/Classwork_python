# Функция принимает на вход словарь, содержащий ФИО и сумму задолженности за коммунальные услуги,
# а возвращает словарь с общим количеством должников и суммой всех долгов, с ключами debtors и total.
def get_debts(people):
    debtors = 0
    for key in people:
        if people.values() > 0:
            debtors += 1
        sum_of_values = sum(people.values())
    return sum_of_values



def test_get_debts():
    input = {'Сырым': 0, 'Адилхан': 100, 'Зульфия': 250}
    expect = {'debtors': 2, 'total': 350}
    assert get_debts(input) == expect

    input = {}
    expect = {'debtors': 0, 'total': 0}
    assert get_debts(input) == expect

test_get_debts()
