from PyQt5.QtWidgets import *
import os
import sys

# Set-ExecutionPolicy -Scope CurrentUser RemoteSigned - чтобы заработало виртуальное окружение
# Set-ExecutionPolicy RemoteSigned -Scope Process - (первый вариант - не точно)
# https://ru.stackoverflow.com/questions/935212/powershell-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B5%D0%B2-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%BE-%D0%B2-%D1%8D%D1%82%D0%BE%D0%B9-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"


class SimpleCalcView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        self.calculator_buttons()

    def calculator_buttons(self):
        layout = QVBoxLayout()
        self.label = QLabel("0")
        layout.addWidget(self.label)

        grid_of_buttons = QGridLayout()
        calc_buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ",", "=", "/"
        ]

        row, column = 1, 0

        for nums in calc_buttons:
            button = QPushButton(nums)
            grid_of_buttons.addWidget(button, row, column)

            column = (column + 1) % 4
            if column == 0:
                row += 1

        layout.addLayout(grid_of_buttons)
        self.setLayout(layout)

def calculator_activate():
    app = QApplication([])
    calculator = SimpleCalcView()
    calculator.show()
    app.exec_()

calculator_activate()

class AccountCalcView(SimpleCalcView):
    def __init__(self):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)

        keys = ('(', ')', '%', '')

        for r in range(len(keys)):
            key = keys[r]
            if key:
                btn = QPushButton(text = key)
                btn.clicked.connect(self.on_button_pressed)
                if key != '%':
                    keys_layout.addWidget(btn, 0, r)
                else:
                    keys_layout.addWidget(btn, 0, r, 1, 2)
