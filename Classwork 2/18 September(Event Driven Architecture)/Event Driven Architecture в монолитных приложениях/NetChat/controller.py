from PyQt6.QtCore import QObject, pyqtSignal
from logger import log

# тут будет контроллер
# state, signal, transition(переход)

class Controller(QObject):
    # DB - DataBase
    # AUTH - Authentification
    _state = "INIT"
    _transitions = (
        {'from' : "INIT",       'to': "LOGIN",          'by': "DB_READY"},
        {'from' : "LOGIN",      'to': "AUTH",           'by': "GUI_LOGIN"},
        {'from' : "AUTH",       'to': "MAIN_WINDOW",    'by': "DB_AUTH_OK"},
        {'from' : "AUTH",       'to': "LOGIN",          'by': "DB_AUTH_BAD"},

        {'from' : "MAIN_WIN",   'to': "ADD_FRIEND",     'by': "UR_HELLO"},
        {'from' : "ADD_FRIEND", 'to': "MAIN_WIN",       'by': "IMMEDIATELY"},

        {'from' : "MAIN_WIN",   'to': "CHECK_MSG",      'by': "UR_MESSAGE"},
        {'from' : "CHECK_MSG",  'to': "MAIN_WIN",       'by': "IMMEDIATELY"},

        {'from' : "MAIN_WIN",   'to': "SEND_MSG",       'by': "GUI_SEND"},
        {'from' : "GUI_SEND",   'to': "MAIN_WIN",       'by': "IMMEDIATELY"},

        {'from' : "MAIN_WIN",   'to': "CHANGING_CHAT",  'by': "GUI_CHAT_CHANGE"},
        {'from' : "CHANGING_CHAT",   'to': "MAIN_WIN",  'by': "IMMEDIATELY"},

    )

    def process_state(self):
        match self.state:
            case "INIT":
                pass
            case "LOGIN":
                pass
            case "AUTH":
                pass
            case "MAIN_WIN":
                pass

            case _:
                log.w("Unknown state!")


    def process_signal(self, signal_name):
        pass
        # BY


    switchWindow = pyqtSignal(str, str)

    def login(self, username):
        if username:
            self.switchWindow.emit('MainWindow', username)
    
    def message_received(self, message_text, message_type):
        log.d(f'Получили сообщеие: {message_text} тип: {message_type}')
