from PyQt6.QtCore import QThread

class UdpSender(QThread):
    def run(self):
        print("Udp sender запущен")

if __name__ == "__main__":
    pass
    # Здесь тестим класс UdpSender
