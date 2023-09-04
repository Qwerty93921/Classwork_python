import sys
from PyQt5.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from Calculator_1 import Calculator
from calc_main_window import *

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создание приложения

    window = CalcMainWindow("Qalculus v. 1.0") # Название приложения
    view = Calculator()

    window.set_view(view) # Внутри окна то что в скобках
    window.show() # Показать
    app.exec() # Запуск приложения
