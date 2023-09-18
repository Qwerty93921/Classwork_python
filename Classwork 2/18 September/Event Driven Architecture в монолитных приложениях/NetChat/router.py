from PyQt6.QtCore import QObject
from gui import Gui
from data_storage import DataStorage
from udp_receiver import UdpReceiver
from udp_sender import UdpSender

# From название папки.название файла import Класс БЕЗ СКОБОК

# from udp_receiver.udp_receiver import UdpReceiver
# Чтобы не писать длинный путь

# from udp_sender.udp_sender import UdpSender
# from gui.gui import Gui
# from data_storage.data import DataStorage

# Создание виртуального окружения
# python -m venv venv
# .\venv\Scripts\activate
# pip install PyQt6
# pip freeze > requirements.txt

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()

        # Здесь будем роутить сигналы
    
    def start(self):
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()
    
    def stop(self):
        self.data_storage.stop()
        self.gui.stop()
        self.udp_receiver.stop()
        self.udp_sender.stop()
