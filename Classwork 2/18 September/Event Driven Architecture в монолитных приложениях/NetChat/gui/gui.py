from PyQt6.QtCore import QThread

class Gui(QThread):
    def run(self):
        print("Интерфейс запущен")