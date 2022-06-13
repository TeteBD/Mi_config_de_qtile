#!/bin/env python3

# TeteBD
# https://github.com/TeteBD

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from libqtile.command.client import InteractiveCommandClient
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os


class power(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú de apagado")
        self.setFixedSize(164, 278)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("background-color:#263238;")

        # Botón 1:
        button_1 = QPushButton("Apagar ", self)
        button_1.setGeometry(28, 20, 110, 40)
        button_1.clicked.connect(self.shutdown)
        button_1.setStyleSheet("background-color:#2d393f;"
                               "border:2px solid #555555cc;"
                               "border-radius:8px;"
                               "color:#a3a9ac")

        # Botón 2:
        button_2 = QPushButton("Reiniciar 勒", self)
        button_2.setGeometry(28, 70, 110, 40)
        button_2.clicked.connect(self.reboot)
        button_2.setStyleSheet("background-color:#2d393f;"
                               "border:2px solid #555555cc;"
                               "border-radius:8px;"
                               "color:#a3a9ac")

        # Botón 3:
        button_3 = QPushButton('Cerrar sesión', self)
        button_3.setGeometry(28, 120, 110, 40)
        button_3.clicked.connect(self.logout)
        button_3.setStyleSheet("background-color:#2d393f;"
                               "border:2px solid #555555cc;"
                               "border-radius:8px;"
                               "color:#a3a9ac")

		# Botón 4:
        button_4 = QPushButton('Suspender ', self)
        button_4.setGeometry(28, 170, 110, 40)
        button_4.clicked.connect(self.suspend)
        button_4.setStyleSheet("background-color:#2d393f;"
                               "border:2px solid #555555cc;"
                               "border-radius:8px;"
                               "color:#a3a9ac")

        # Botón 5:
        button_5 = QPushButton('Cerrar ', self)
        button_5.setGeometry(28, 220, 110, 40)
        button_5.clicked.connect(self.exit)
        button_5.setStyleSheet("background-color:#2d393f;"
                               "border:2px solid #555555cc;"
                               "border-radius:8px;"
                               "color:#a3a9ac")


    def shutdown(self):
        os.system("shutdown now")

    def reboot(self):
        os.system("reboot")

    def logout(self):
        command = InteractiveCommandClient()
        print(command.shutdown())

    def suspend(self):
        window.hide()
        os.system("systemctl suspend")
        sys.exit()

    def exit(self):
        sys.exit()



app = QApplication(sys.argv)
window = power()
window.show()
app.exec_()
