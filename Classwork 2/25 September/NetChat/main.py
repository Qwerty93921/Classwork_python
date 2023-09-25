import sys
from logger import Logger
from PyQt6.QtWidgets import QApplication
from router import Router

if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = Logger(Logger.DEBUG)

    route = Router()
    route.start()

    app.exec()
