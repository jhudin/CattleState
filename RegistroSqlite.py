import hashlib
import random
import sqlite3
import smtplib
import this
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegularExpression, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QSystemTrayIcon
import ctypes
from LoginSqlite3 import *
import fondo_rc
class RegistroU(object):
    def setupUi(self, Registro):
        myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        Registro.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"),Registro)
        Registro.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
        Registro.setObjectName("Registro")
        Registro.resize(545, 608)
        Registro.setMinimumSize(QtCore.QSize(545, 608))
        Registro.setMaximumSize(QtCore.QSize(545, 608))
        Registro.setStyleSheet("*{font: 26pt Tw Cen MT Condensed;\n"
"font-size:26px;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    \n"
"background-image: url(:/Fondos/Imagenes/green-leaves-pattern-background-flat-lay-nature-dark-green-tone-background_9635-1311.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(47, 53, 66, .97);\n"
"border-radius:15px;\n"
"border:1px solid black;\n"
"}\n"
"\n"
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
"background:rgba(47, 53, 66, 1);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Registro)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 80, 381, 521))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 341, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.Nombre = QtWidgets.QLineEdit(self.frame)
        self.Nombre.setGeometry(QtCore.QRect(30, 140, 311, 41))
        self.Nombre.setText("")
        self.Nombre.setObjectName("Nombre")
        self.Usuario = QtWidgets.QLineEdit(self.frame)
        self.Usuario.setGeometry(QtCore.QRect(30, 260, 311, 41))
        self.Usuario.setText("")
        self.Usuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Usuario.setObjectName("Usuario")
        self.clave = QtWidgets.QLineEdit(self.frame)
        self.clave.setGeometry(QtCore.QRect(30, 320, 311, 41))
        self.clave.setText("")
        self.clave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clave.setObjectName("clave")
        self.Correo = QtWidgets.QLineEdit(self.frame)
        self.Correo.setGeometry(QtCore.QRect(30, 200, 311, 41))
        self.Correo.setText("")
        self.Correo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Correo.setObjectName("Correo")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 50, 161, 61))
        self.label.setStyleSheet("font: 75 72pt \"Bahnschrift Condensed\";")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.clave_2 = QtWidgets.QLineEdit(self.frame)
        self.clave_2.setGeometry(QtCore.QRect(30, 380, 311, 41))
        self.clave_2.setText("")
        self.clave_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clave_2.setObjectName("clave_2")
        self.pbut2 = QtWidgets.QPushButton(self.frame)
        self.pbut2.setGeometry(QtCore.QRect(20, 490, 341, 23))
        self.pbut2.setStyleSheet("#pbut2{\n"
"background:transparent;\n"
"border:1px solid transparent;\n"
"    font: 12pt ;\n"
"    text-decoration: underline;\n"
"}\n"
"#pbut2:hover{\n"
"color:white;\n"
"}")
        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        try:
            cursor.execute("CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre varchar (50),correo varchar (50),usuarios varchar (50),clave varchar (50))")
        except Exception as e:
            print()
        conection.close()
        self.pbut2.setObjectName("pbut2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setEnabled(True)
        self.toolButton.setGeometry(QtCore.QRect(220, 10, 121, 121))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/Imagenes/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setAutoRepeatInterval(100)
        self.toolButton.setObjectName("toolButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(220, 10, 120, 121))
        self.frame_2.setStyleSheet("\n"
"background:transparent;\n"
"border:1px solid transparent;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        Registro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Registro)
        QtCore.QMetaObject.connectSlotsByName(Registro)
        Registro.setTabOrder(self.Nombre, self.Correo)
        Registro.setTabOrder(self.Correo, self.Usuario)
        Registro.setTabOrder(self.Usuario, self.clave)
        Registro.setTabOrder(self.clave, self.clave_2)
        Registro.setTabOrder(self.clave_2, self.pushButton)
        Registro.setTabOrder(self.pushButton, self.toolButton)
        self.pushButton.clicked.connect(lambda: self.Registrar(Registro))
        self.pbut2.clicked.connect(lambda : self.Ingresar(Registro))


    def retranslateUi(self, Registro):
        _translate = QtCore.QCoreApplication.translate
        Registro.setWindowTitle(_translate("Registro", "Registro"))
        self.pushButton.setText(_translate("Registro", "REGISTRAR"))
        self.Nombre.setPlaceholderText(_translate("Registro", "NOMBRE"))
        self.Usuario.setPlaceholderText(_translate("Registro", "USUARIO"))
        self.clave.setPlaceholderText(_translate("Registro", "CONTRASEÑA"))
        self.Correo.setPlaceholderText(_translate("Registro", "CORREO"))
        self.label.setText(_translate("Registro", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">REGISTRO</span></p></body></html>"))
        self.clave_2.setPlaceholderText(_translate("Registro", "REPETIR CONTRASEÑA"))
        self.pbut2.setText(_translate("Registro", "¿Ya posee cuenta? , Ingresar"))

    def Registrar(self,Registro):
        correocor=bool
        clavecorr=bool
        reg_ex = QRegExp("\\b[a-z-A-Z0-9._%+-]+@[a-z-A-Z0-9.-]+\\.[a-z-A-Z]{2,4}\\b")
        le_username_validator = QRegExpValidator(reg_ex, self.Correo)
        self.Correo.setValidator(le_username_validator)
        if ((self.Correo.hasAcceptableInput()) == False):
            correocor=False
        else:
            correocor = True

        reg_ex = QRegExp("^([0-9-A-Z-a-z]){6,100}$")
        le_username_validator = QRegExpValidator(reg_ex, self.clave)
        self.clave.setValidator(le_username_validator)
        if ((self.clave.hasAcceptableInput()) == False):
            clavecorr = False
        else:
            clavecorr = True


        nombre = self.Nombre.text()
        usuario = self.Usuario.text()
        correo = self.Correo.text()
        clave = self.clave.text()
        clave2 = self.clave_2.text()

        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        valor = False
        for Dato in resultados:
            users = str(Dato[3])
            if users == usuario:
                valor = True
        cursor.close()
        conection.close()
        if (nombre != "" and usuario != "" and correo != ""):
            if (correocor):
                self.Correo.setStyleSheet("QLineEdit { color: white;}");
                if (valor == False):
                    self.Usuario.setStyleSheet("QLineEdit { color: white;}");
                    if (clavecorr):
                        self.clave.setStyleSheet("QLineEdit { color: white;}");
                        if (clave == clave2):
                            self.clave_2.setStyleSheet("QLineEdit { color: white;}");
                            m = hashlib.sha512()
                            m.update((clave).encode('utf-8'))
                            claveen = m.hexdigest()
                            conection=sqlite3.connect("data/dat")
                            cursor=conection.cursor()
                            valores = "INSERT INTO usuario(`nombre`, `correo`, `usuarios`, `clave`) VALUES(?,?,?,?)"
                            cursor.execute(valores, (
                                nombre, correo.lower(), usuario, claveen))
                            conection.commit()
                            conection.close()
                            try:
                                QMessageBox.information(Registro, 'Correcto', 'La informacion ha sido almacenada')
                                conection.close()
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
                                if (valor<=1):
                                    from RegistroHato import RHato
                                    import sys
                                    myappid = 'Guayaba_java.CatleState.Catle.0.1' # arbitrary string
                                    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
                                    self.w = QtWidgets.QMainWindow()
                                    self.w.systray = QSystemTrayIcon(QIcon("Imagenes/Logo1.2.ico"), self.w)
                                    self.w.setWindowIcon(QtGui.QIcon('Imagenes/Logo1.2.ico'))
                                    self.ui = RHato()
                                    self.ui.setupUi(self.w)
                                    self.w.show()
                                    Registro.close()
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
                            except Exception as e:
                                QMessageBox.critical(Registro, 'Error', 'error al guardar la informacion')
                        else:
                            QMessageBox.critical(Registro, 'Error', 'Las contraseñas no coinciden')
                            self.clave_2.setStyleSheet("QLineEdit { color: red;}");
                    else:
                        QMessageBox.critical(Registro, 'Error', 'La contraseña debe tener mas de 6 digitos')
                        self.clave.setStyleSheet("QLineEdit { color: red;}");
                else:
                    QMessageBox.critical(Registro, 'Error', 'El usuario ya existe')
                    self.Usuario.setStyleSheet("QLineEdit { color: red;}")
            else:
                QMessageBox.critical(Registro, 'Error', 'El Correo se encuentra en un formato invalido')
                self.Correo.setStyleSheet("QLineEdit { color: red;}");
        else:
            QMessageBox.critical(Registro, 'Error', 'Asegurece de llenar todos os campos')
    def Ingresar(self,Registro):
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





