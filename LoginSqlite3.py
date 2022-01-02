# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import hashlib
import sqlite3
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMessageBox, QApplication
import ctypes
from RegistroSqlite import *
from RegistroAnimal import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        MainWindow.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"), MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 608)
        MainWindow.setMinimumSize(QtCore.QSize(545, 608))
        MainWindow.setMaximumSize(QtCore.QSize(545, 608))
        MainWindow.setStyleSheet("*{font: 26pt Tw Cen MT Condensed;\n"
"font-size:26px;\n"
"\n"
"}\n"
"#centralwidget{background-image: url(:/Fondos/Imagenes/green-leaves-pattern-background-flat-lay-nature-dark-green-tone-background_9635-1311.jpg);"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(47, 53, 66,.97);\n"
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
"background:rgba(16, 172, 132,1.0);\n"
"color:black;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border-radius:5px;\n"
"background:rgba(87, 101, 116,1.0);\n"
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
        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        try:
            cursor.execute("CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre varchar (50),correo varchar (50),usuarios varchar (50),clave varchar (50))")
        except Exception as e:
            print()
        conection.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 90, 381, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 341, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.Usuario = QtWidgets.QLineEdit(self.frame)
        self.Usuario.setGeometry(QtCore.QRect(30, 200, 311, 41))
        self.Usuario.setText("")
        self.Usuario.setObjectName("Usuario")
        self.clave = QtWidgets.QLineEdit(self.frame)
        self.clave.setGeometry(QtCore.QRect(30, 300, 311, 41))
        self.clave.setText("")
        self.clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clave.setObjectName("clave")
        self.bont2 = QtWidgets.QPushButton(self.frame)
        self.bont2.setGeometry(QtCore.QRect(20, 440, 341, 31))
        self.bont2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bont2.setStyleSheet("#bont2{background:transparent;\n"
"text-decoration: underline;\n"
"font: 12pt ;\n"
"border:1px solid transparent;\n"
"color:black;}\n"
"#bont2:hover{\n"
"color:white;\n"
"}")
        self.bont2.setObjectName("bont2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(220, 20, 121, 121))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Imagenes/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Usuario, self.clave)
        MainWindow.setTabOrder(self.clave, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.toolButton)
        self.bont2.clicked.connect(lambda : self.registrar(MainWindow))
        self.pushButton.clicked.connect(lambda :self.ingresar(MainWindow))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "INGRESAR"))
        self.Usuario.setPlaceholderText(_translate("MainWindow", "USUARIO"))
        self.clave.setPlaceholderText(_translate("MainWindow", "CONTRASEÑA"))
        self.bont2.setText(_translate("MainWindow", "Registrar Usuario"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">INGRESO</span></p></body></html>"))
    def ingresar(self,MainWindow):
        usuario = self.Usuario.text()
        clave = self.clave.text()

        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        usuariobool = False
        clavbool = False
        correo = ""
        m = hashlib.sha512()
        clav = ""
        m.update((clave).encode('utf-8'))
        claveen = m.hexdigest()
        for Dato in resultados:
            users = str(Dato[3])
            clav = str(Dato[4])
            if users == usuario:
                usuariobool = True
                clav = str(Dato[4])
                if (claveen == clav):
                    clavbool = True
                    correo = str(Dato[2])

        if (usuariobool and clavbool):
            from RegistroAnimal import Ui_Registro
            self.ventana = QtWidgets.QMainWindow()
            self.ventana.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
            self.ui = Ui_Registro()
            self.ui.setupUi(self.ventana)#, correo)
            self.ventana.show()
            MainWindow.setVisible(False)
        else:
            QMessageBox.critical(MainWindow, 'Error', 'Datos incorrectos')
    def registrar(self,MainWindow):
        from RegistroSqlite import RegistroU
        import sys
        myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.w = QtWidgets.QMainWindow()
        self.w.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"), self.w)
        self.w.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
        self.ui = RegistroU()
        self.ui.setupUi(self.w)
        self.w.show()
        MainWindow.close()



import fondo_rc


if __name__ == "__main__":
    import sys
    myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

