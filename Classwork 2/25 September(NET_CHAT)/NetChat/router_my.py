from PyQt6.QtCore import QObject
from logger import Logger
from gui import Gui
from data_storage import DataStorage
from udp_receiver import UdpReceiver
from udp_sender import UdpSender
from controller import Controller

log = Logger.Instance

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

# pip install pyqt6-tools(Новый урок)
# pyqt6-tools designer(Запуск программы "Qt Designer")
# Создать большую рамку ГОРИЗОНТАЛЬНУЮ и ВНУТРЬ нее вставить остальные 3 РАМКИ
# Первая рамка вертикальная остальные 3 горизонтальные
# В НИЖНЮЮ горизонтальную рамку добавить "Text edit"
# СПРАВА СНИЗУ добавить "Push button" с надписью "Отправить"
# Класс QFrame почти везде
# СВЕРХУ в рамку добавить "TEXT BROWSER"

# https://habr.com/ru/companies/skillfactory/articles/599599/
# PyQt6 ГАЙД ДЛЯ НОВИЧКОВ

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()
        self.controller = Controller()
        self.gui.sendMessage.connect(lambda s: print(s))
        self.gui.loginUser.connect(self.data_storage.auth)
        self.gui.loginUser.connect(self.controller)
        self.controller.switchWindow.connect(self.gui.set_window)

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
