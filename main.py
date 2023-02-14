import sys, subprocess
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint

class ClGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.si.clicked.connect(self.felicidades)
        self.no.enterEvent = self.move_button
        self.algo = True
    
    def felicidades(self):
        GUI.destroy()
        subprocess.run("python main2.py")

    def move_button(self, Event):
        if self.algo == True:
            # Obtiene la posición actual del botón
            current_pos = self.no.pos()

            # Calcula la nueva posición en el eje x
            new_pos_x = current_pos.x() - 380

            # Mueve el botón a la nueva posición
            self.no.move(new_pos_x, current_pos.y())

            # Obtiene la posición actual del botón
            current_pos = self.si.pos()

            # Calcula la nueva posición en el eje x
            new_pos_x = current_pos.x() + 380

            # Mueve el botón a la nueva posición
            self.si.move(new_pos_x, current_pos.y())
            self.algo = False
        else:
             # Obtiene la posición actual del botón
            current_pos = self.no.pos()

            # Calcula la nueva posición en el eje x
            new_pos_x = current_pos.x() + 380

            # Mueve el botón a la nueva posición
            self.no.move(new_pos_x, current_pos.y())

            # Obtiene la posición actual del botón
            current_pos = self.si.pos()

            # Calcula la nueva posición en el eje x
            new_pos_x = current_pos.x() - 380

            # Mueve el botón a la nueva posición
            self.si.move(new_pos_x, current_pos.y())
            self.algo = True
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    GUI = ClGUI()
    GUI.setWindowTitle("Especial San-Valentin")
    GUI.show()
    sys.exit(app.exec_())