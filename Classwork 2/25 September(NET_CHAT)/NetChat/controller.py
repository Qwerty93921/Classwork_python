from PyQt6.QtCore import QObject, pyqtSignal

# тут будет контроллер
class Controller(QObject):
    switchWindow = pyqtSignal(str, str)
    def login(self, username):
        if username:
            self.switch_window.emit('MainWindow', username)