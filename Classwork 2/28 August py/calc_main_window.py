from PyQt5.QtWidgets import QMainWindow
from Calculator_1 import Calculator

class CalcMainWindow(QMainWindow): # Унаследование от QMainWindow
    calc_view = None # Самописная функция
    
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

    def set_view(self, view): # Самописная функция
        self.calc_view = view
        self.setCentralWidget(self.calc_view)
