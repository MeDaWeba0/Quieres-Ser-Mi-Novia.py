import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint

class ClGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui1.ui", self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    GUI = ClGUI()
    GUI.setWindowTitle("Especial San-Valentin")
    GUI.show()
    sys.exit(app.exec_())