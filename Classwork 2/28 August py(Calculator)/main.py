import sys
from PyQt5.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import Calculator
from calc_main_window import *
from calc_control import CalcControlWidget
from calc_model import AccountCalcModel

def switch_mode(name):
    if name == "Account":
        model = AccountCalcModel()
        view = AccountCalcView()
        view.set_model(model)
        window.set_view(view)

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создание приложения

    window = CalcMainWindow("Qalculus v. 1.0") # Название приложения
    model = AccountCalcModel()
    view = Calculator()
    switch = CalcControlWidget()
    switch.swithed.connect(switch_mode)
    window.set_switcher(switch)

    window.set_view(view) # Внутри окна то что в скобках
    window.show() # Показать
    app.exec() # Запуск приложения
