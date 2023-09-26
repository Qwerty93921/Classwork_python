from PyQt6.QtCore import QThread, pyqtSignal
import socket
import time
from logger import log
import threading

class UdpSender(QThread):
    _queue = []
    sent = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False
        self.lock = threading.Lock()



    def run(self):
        log.i("Udp sender запущен") # i() - метод info показывает сообщение
        self.running = True
        while self.running:
            if len(self._queue) > 0:
                self.lock.acquire()
                msg, msg_type = self._queue.pop()
                self.lock.release()
                self.socket.sendto(msg.encode(), self.addres)
                self.sent.emit(msg)
            else:
                time.sleep(0.025)
    
    def send(self, message, message_type):
        self.lock.acquire()
        self._queue.append((message, message_type,))
        self.lock.release()

    def stop(self):
        self.running = False
        super().stop()


if __name__ == "__main__":
    pass
    # Здесь тестим класс UdpSender
