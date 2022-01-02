from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        try:
            cursor.execute("CREATE TABLE Ranimales(id INTEGER PRIMARY KEY AUTOINCREMENT,codigo int (11),nombre varchar (50),fnacimiento varchar (50),mingreso varchar (50),fingreso varchar (50),raza varchar (50),sexo varchar (50),lote varchar (50),crias int (11),peso varchar (50),procedencia varchar (50),estado varchar (50),salud varchar (50),hregistro varchar (50),produccion varchar (50),color varchar (50),rutfot varchar (150))")
        except Exception as e:
            print()
        conection.close()

self.pushButton.clicked.connect(lambda: self.RegistroAnimal(self.tabWidget))
        rutafoto =self.BImport.clicked.connect(lambda : self.buscarArchivo(Registro))

        conection=sqlite3.connect("data/dat")
        sql="SELECT * FROM Ranimales"
        result=conection.execute(sql)
        self.tableWidget_4.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget_4.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))
        conection.close()
        reg_ex = QRegExp("^([0-9]){6,100}$")
        le_username_validator = QRegExpValidator(reg_ex, self.codigoText)
        self.codigoText.setValidator(le_username_validator)

def RegistroAnimal(self,tabWidget):
        
        codigo=self.codigoText.text()
        nombre = self.NombreText.text()
        fnacimiento=self.EditNacimiento.text()
        mingreso=str(self.MIngreso.currentText())
        fingreso=self.FIngreso.text()
        raza=str(self.comboBox.currentText())
        sexo=str(self.sexo.currentText())
        ubicacion=str(self.ubicacion.currentText())
        crias=0
        produccion=self.Peso_2.text()
        if (self.checkBox.isChecked==False):
            crias=0
            produccion=0
        crias=self.crias.text()
        Peso=self.Peso.text()
        L_Procedencia=str(self.L_Procedencia.currentText())
        Estado=str(self.Estado.currentText())
        Est_Salud=str(self.Est_Salud.currentText())
        hora_Reg=self.hora_Reg.text()
        color=self.lineEdit.text()
        rutafot=self.rutaed.text()

        print()
        
        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        valores = "INSERT INTO Ranimales(codigo,nombre ,fnacimiento,mingreso ,fingreso,raza ,sexo,lote,crias,peso ,procedencia,estado ,salud,hregistro,produccion,color,rutfot) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(valores,(codigo,nombre,fnacimiento,mingreso,fingreso,
            raza,sexo,ubicacion,crias,Peso,L_Procedencia,Estado,Est_Salud,hora_Reg,produccion,color,rutafot))
        conection.commit()
        conection.close()
        try:
            QMessageBox.information(Registro, 'Correcto', 'La informacion ha sido almacenada')
            conection.close()
            self.codigoText.setText("")
            self.NombreText.setText("")
            self.Peso_2.setValue(0)
            self.crias.setValue(0)
            self.Peso.setValue(0)

            self.lineEdit.setText("")
            self.rutaed.setText("")
            tabWidget.setCurrentIndex(0)
        except Exception as e:
            QMessageBox.critical(Registro, 'Error', 'error al guardar la informacion')
            print(e)

def buscarArchivo(self, Registro):
	fname, _ = QFileDialog.getOpenFileName(Registro, 'Open File', '', "Image Files (*.jpg *.png)")
	if fname:
	    pixmap = QPixmap(fname)
	    pixi = pixmap.scaledToWidth(self.foto.width())
	    self.foto.setPixmap(pixi)
	    self.rutaed.setText(fname)
