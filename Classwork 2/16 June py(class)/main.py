from person import Person
from kassa import Kassa
from train import Train

if __name__ == "__main__":

    print("Главная программа", __name__)

    Elon = Person("Elon Musk", 55)
    Elon.earn(97000)
    Elon.pay(13000)
    Elon.show()

    # test_ticket = Ticket("Алматы", "Сантьяго", test_man.name, test_man.iin, test_man.age)
    # test_ticket.show()

    almaty1 = Kassa()
    price = almaty1.get_price("Алматы", "Сантьяго")
    almaty1.buy_ticket("Алматы", "Сантьянго", Elon)
    almaty1.buy_ticket("Астана", "Калькутта", Elon)


    train = Train(almaty1, "Алматы", "Сантьянго")
    train.show()

    print(almaty1.tickets)
    train.board(Elon)
    print(almaty1.tickets)
