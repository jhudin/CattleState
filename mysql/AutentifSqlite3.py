# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Autentif.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import smtplib

from PyQt5.QtWidgets import QMessageBox

from RegistroAnimal import *


class Autentif(object):
    def setupUi(self, MainWindow,correo):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 474)
        MainWindow.setMinimumSize(QtCore.QSize(545, 474))
        MainWindow.setMaximumSize(QtCore.QSize(545, 474))
        MainWindow.setStyleSheet("*{font-family:Bahnschrift Condensed;\n"
"font-size:22px;\n"
"\n"
"}\n"
"#centralwidget{\n"
"    \n"
"    \n"
"    \n"
"    background-image: url(:/newPrefix/4a4c046a0390ce57387bbe8284156652.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(47, 53, 66,1);\n"
"border-radius:15px;\n"
"border:1px solid black;\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#d1d8e0;\n"
"border-radius:60px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"border:none;}\n"
"\n"
"QPushButton{\n"
"background:#22a6b3;\n"
"color:black;\n"
"border-radius:5px;\n"
"border:1px solid black;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border-radius:5px;\n"
"background:gray;\n"
"border:qpx solid white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"QMessageBox{\n"
"background:rgba(47, 53, 66, 1);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 90, 381, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 341, 51))
        self.pushButton.setObjectName("pushButton")
        self.codig_corre = QtWidgets.QLineEdit(self.frame)
        self.codig_corre.setGeometry(QtCore.QRect(30, 210, 311, 41))
        self.codig_corre.setText("")
        self.codig_corre.setObjectName("codig_corre")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(-20, 110, 401, 91))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(220, 20, 121, 121))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/Imagenes/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setAutoRepeatInterval(100)
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 120, 191, 91))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(220, 20, 121, 121))
        self.frame_2.setStyleSheet("background:transparent;\n"
"border:1px solid transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)

        global cod;cod = random.randint(1000, 9999)
        subject = "Codigo de Verificacion"
        codStr = cod.__str__()
        codStr = "Subject: {}\n\n{}".format(subject, codStr)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('jhudinvin@gmail.com', 'Perro123456')
        server.sendmail('jhudinvin@gmail.com', correo, codStr)
        server.quit()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.codig_corre, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.toolButton)
        self.pushButton.clicked.connect(lambda : self.validar(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autenticacion"))
        self.pushButton.setText(_translate("MainWindow", "Validar"))
        self.codig_corre.setPlaceholderText(_translate("MainWindow", "CODIGO"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Al correo vinculado ha sido eviado un codigo de</p><p align=\"center\"> verificacion , ingreselo para continuar</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">VALIDAR</span></p></body></html>"))

    def validar(self,MainWindow):
        if(cod.__str__()==self.codig_corre.text()):
            self.ventana = QtWidgets.QMainWindow()
            self.ui = RegistroAnimal()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            MainWindow.destroy()
        else:
            QMessageBox.critical(MainWindow, 'Error', 'Codigo de verificacion incorrecto')

import fondo_rc


