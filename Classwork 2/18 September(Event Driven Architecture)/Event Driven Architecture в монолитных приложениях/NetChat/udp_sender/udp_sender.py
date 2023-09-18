from PyQt6.QtCore import QThread

class UdpSender(QThread):
    def run(self):
        print("Udp sender запущен")