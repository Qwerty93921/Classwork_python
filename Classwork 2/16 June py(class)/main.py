from person import Person
from kassa import Kassa
from train import Train



test_man = Person("Elon Musk", 55)
test_man.earn(30000)
test_man.pay(13000)
test_man.show()

# test_ticket = Ticket("Алматы", "Сантьяго", test_man.name, test_man.iin, test_man.age)
# test_ticket.show()

kassa = Kassa()
price = kassa.get_price("Алматы", "Сантьяго")
kassa.buy_ticket("Алматы", "Сантьянго", test_man)


if test_man.ticket:
    test_man.ticket.show()

train = Train("Алматы", "Сантьянго")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("Билета больше нет")
