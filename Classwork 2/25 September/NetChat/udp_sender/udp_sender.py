from PyQt6.QtCore import QThread
from time import sleep
# неуверен что правильный модуль

class UdpSender(QThread):
    _queue = []

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False

    def run(self):
        log.i("Udp sender запущен") # i() - метод info показывает сообщение
        self.running = True
        while self.running:
            if len(self._queue) > 0:
                msg, msg_type = self._queue.pop()
                self.socket.sendto(msg.encode(), self.addres)
            else:
                time.sleep(0.025)
    
    def send(self, message, message_type):
        self._queue.append((message, message_type,))

if __name__ == "__main__":
    pass
    # Здесь тестим класс UdpSender
