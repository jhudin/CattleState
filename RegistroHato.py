# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroHato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import hashlib
import random
import sqlite3
import smtplib
import this
from PyQt5.QtCore import QRegularExpression, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QSystemTrayIcon
import ctypes
from LoginSqlite3 import *
import fondo_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class RHato(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 354)
        MainWindow.setStyleSheet("*{font: 26pt Tw Cen MT Condensed;\n"
"font-size:18px;\n"
"background:rgba(47, 53, 66, .87);\n"
"}\n"
"#title{\n"
"border-radius:1px;\n"
"background:rgba(47, 53, 66, 1);\n"
"font-size:22px;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius: 7px;\n"
"color:white;\n"
"border:1px solid black;\n"
"}\n"
"\n"
"#centralwidget{\n"
"}\n"
"#frame{\n"
"background:rgba(47, 53, 66, .95);\n"
"}\n"
"QFrame{\n"
"border:1px solid black;\n"
"background:rgba(47, 53, 66, .95);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius: 7px;\n"
"}\n"
"#line{\n"
"background:black;}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"background:transparent;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background:rgba(16, 172, 132,1.0);\n"
"color:black;\n"
"border-radius:3px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(200, 214, 229,1.0);\n"
"border-radius:5px;\n"
"background:rgba(87, 101, 116,1.0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"color:white;\n"
"background:transparent;\n"
"border:none;\n"
"\n"
"border-bottom:1px solid white;\n"
"}\n"
"QComboBox{\n"
"color:white;\n"
"background:transparent;\n"
"border:none;\n"
"\n"
"border-bottom:1px solid white;;\n"
"\n"
"}\n"
"QSpinBox{\n"
"color:white;\n"
"background:transparent;\n"
"border:none;\n"
"\n"
"border-bottom:1px solid white;\n"
"}\n"
"#spinBox{\n"
"color:white;\n"
"font:center;}\n"
"\n"
"QTimeEdit{\n"
"color:white;\n"
"background:transparent;\n"
"border:none;\n"
"\n"
"border-bottom:1px solid white;\n"
"}\n"
"#foto{\n"
"border:1px solid white;}\n"
"QRadioButton{\n"
"color:white;\n"
"}\n"
"QTabBar{\n"
"font: 26pt Tw Cen MT Condensed;\n"
"font-size:23px;\n"
"color:rgba(127, 140, 141,.9);\n"
"background:transparent;\n"
"\n"
"}\n"
"QTabBar::tab:hover{\n"
"color:rgba(47, 53, 66, 1);\n"
"background:rgba(127, 140, 141,.9);\n"
"}\n"
"QTabBar::tab{\n"
"background:rgba(47, 53, 66, .87);\n"
"border-right:1px solid #34495e;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius: 7px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"font: 26pt Tw Cen MT Condensed;\n"
"font-size:23px;\n"
"color:white;\n"
"background:rgba(127, 140, 141,.9);\n"
"}\n"
"QCalendarWidget{\n"
"background:rgba(127, 140, 141,.9);}\n"
"")
        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        try:
            cursor.execute("CREATE TABLE Hato(id INTEGER PRIMARY KEY AUTOINCREMENT,nombreH varchar (50),tel int (20),ubicaion varchar (50),correo varchar (50),Nombre_enH varchar (50))")
        except Exception as e:
            print()
        conection.close()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda :self.RegistrarH(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">REGISTRAR HATO</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "TELEFONO DE CONTACTO "))
        self.label_4.setText(_translate("MainWindow", "UBICACIÓN-DIRECCION"))
        self.label_2.setText(_translate("MainWindow", "NOMBRE HATO"))
        self.label_5.setText(_translate("MainWindow", "CORREO DE CONTACTO"))
        self.label_6.setText(_translate("MainWindow", "NOMBRE ENCARGADO"))
        self.pushButton.setText(_translate("MainWindow", "REGISTRAR"))

    def RegistrarH(self,Registro):

        nombre = self.lineEdit.text()

        tel = self.lineEdit_2.text()

        ubica = self.lineEdit_3.text()

        correo = self.lineEdit_4.text()


        Nombre_encar = self.lineEdit_5.text()

        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        valor = 0
        for Dato in resultados:
            valor+=1
        cursor.close()
        conection.close()
        if (valor==0):
            conection=sqlite3.connect("data/dat")
            cursor=conection.cursor()
            valores = "INSERT INTO Hato(nombreH,tel,ubicaion,correo,Nombre_enH) VALUES(?,?,?,?,?)"
            cursor.execute(valores, (
                nombre, tel, ubica, correo,Nombre_encar))
            conection.commit()
            conection.close()
            try:
                QMessageBox.information(Registro, 'Correcto', 'La informacion ha sido almacenada')
                conection.close()
                from LoginSqlite3 import Ui_MainWindow
                import sys
                myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
                self.w = QtWidgets.QMainWindow()
                self.w.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"), self.w)
                self.w.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.w)
                self.w.show()
                Registro.close()
            except Exception as e:
                QMessageBox.critical(Registro, 'Error', 'error al guardar la informacion')
        else:
            from LoginSqlite3 import Ui_MainWindow
            import sys
            myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            self.w = QtWidgets.QMainWindow()
            self.w.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"), self.w)
            self.w.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.w)
            self.w.show()
            Registro.close()
            
