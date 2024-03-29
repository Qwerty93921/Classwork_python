from logger import log
from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
from .main_window import MainWindow
from .login_window import LoginWindow
from message import Message


class Gui(QObject):
    sendMessage = pyqtSignal(str)
    loginUser = pyqtSignal(str, str)
    changeChat = pyqtSignal(str)
    window : QWidget = None
    show_message = pyqtSignal(Message)
    add_contact = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        self.running = False

    def start(self):
        self.run()

    def run(self):
        log.i("Интерфэйс запущен")
        

    def set_window(self, window_name, username=None):
        if window_name == type(self.window).__name__:
            return
        self.running = True
        if self.window is not None:
            self.window.hide()
        match window_name: 
            case 'MainWindow':
                self.window = MainWindow(username)
                self.show_message.connect(self.window.show_message)
                self.add_contact.connect(self.window.add_contact)
                self.window.sendMessage.connect(self.sendMessage)
            case 'LoginWindow':
                self.window = LoginWindow()
                self.window.loginUser.connect(self.loginUser)
            case _ : 
                log.e('Неизвестное имя окна:', window_name)
        if self.running:
            self.window.show()

    def set_chat(self, name_chat):
        pass
