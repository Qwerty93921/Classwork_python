from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6 import uic
# uic - загрузчик файлов из .ui
# В терминале написать ------- python main.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)

class Gui(QThread):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()

    def run(self):
        print("Интерфейс запущен")
        button = self.window.findChild(QPushButton, "pushButton") # Меняем текст "Отправить" на "OLOLO"
        button.setText("OLOLO")
