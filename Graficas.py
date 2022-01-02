from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from datetime import datetime, date, timedelta
import calendar
from threading import Timer
#self.tabWidget.currentChanged.connect(lambda: GraficaProd(self.Grafica_am)) #changed!
def GraficaProd(Grafica_am,tabWidget,sv):
    if(tabWidget.currentIndex()==sv):
        series,mañana,tarde,max=getseries()
        chart = QChart()

        chart.addSeries(series)
        chart.setTitle("PRODUCCION SEMANAL")
        categories = ["Lun", "Mar", "Mier", "Juev", "Viern", "Sab","Dom"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.axisY(series).setRange(0, max+(0.1*max))
        chart.axisY(series).setTitleText("LITROS")
        chart.setBackgroundRoundness(0)
        
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart,Grafica_am)
        chartView.setMinimumSize(Grafica_am.width(),Grafica_am.height())#ancho x alto

def valor():
    return True


def getseries():
    conection=sqlite3.connect("data/dat")
    sql="SELECT * FROM ProduccionLech"
    result=conection.execute(sql)
    formato = "%H:%M:%S"
    formatod = "%d/%b/%y"
    tarde=[0,0,0,0,0,0,0]
    tarde1=[0,0,0,0,0,0,0]
    mañana1=[0,0,0,0,0,0,0]
    mañana=[0,0,0,0,0,0,0]
    sumadia=0
    sumañana=0
    dias=""
    i=-1
    max=0
    acum=0
    acut=0
    for Dato in (result):
        hhmmss = datetime.strptime(Dato[1], formato)
        dia = datetime.strptime(Dato[2], formatod)

        if(dia.strftime('%a')=="Mon"):
            i=0
        elif(dia.strftime('%a')=="Tue"):
            i=1
        elif(dia.strftime('%a')=="Wed"):
            i=2
        elif(dia.strftime('%a')=="Thu"):
            i=3
        elif(dia.strftime('%a')=="Fri"):
            i=4
        elif(dia.strftime('%a')=="Sat"):
            i=5
        elif(dia.strftime('%a')=="Sun"):
            i=6
        hora=int(hhmmss.hour)
        produ=(Dato[3])
        produflo=float(produ)
        
        if dias!=Dato[2]:
            dias=Dato[2]
            tarde=tarde1
            mañana=mañana1
            sumadia=0
            acum=0
            acut=0
        if(dias==Dato[2]):
            sumadia+=produflo
        if(max<sumadia):
            max=sumadia
        if(hora>12):
            tarde1=tarde[:]
            tarde1.insert(i,(sumadia-acut))
            acum+=produflo
        if(hora<=12):
            mañana1=mañana[:]
            mañana1.insert(i,(sumadia-acum))
            acut+=produflo
    high = QBarSet("MAÑANA")
    hight = QBarSet("TARDE")
    high.append(mañana1)
    hight.append((tarde1))
    series = QBarSeries()
    series.append(high)
    series.append(hight)
    series.setBarWidth(0.6)
    series.setVisible(True)
    font = QFont()
    font.setFamily('Segoe UI')
    font.setPixelSize(10)
    return series,mañana1,tarde1,max

def onChange(tableWidget_4):
    conection=sqlite3.connect("data/dat")
    sql="SELECT codigo,nombre,sexo,raza,fnacimiento,lote,crias,salud,peso,fingreso FROM Ranimales"
    result=conection.execute(sql)
    tableWidget_4.setRowCount(0)

    for row_number,row_data in enumerate(result):
        tableWidget_4.insertRow(row_number)
        for col_number, data in enumerate(row_data):
            tableWidget_4.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))
    conection.close()  

def EliminarR(tableWidget_4):
        r = int (tableWidget_4.currentRow())
        print(r+1)
def print_row(self,tabWidget):
    if(tabWidget.currentIndex()==3):
        items = self.selectedItems()
        print(items[0].text())

def RProduccion(produccion,Registro,tableWidget_3,Grafica_am,tab):
    a=produccion.text()
    if(a!="0"):
        mañana=[]
        tarde=[]
        fechactual=time.strftime("%d/%b/%y")
        hora=time.strftime("%X")
        conection=sqlite3.connect("data/dat")
        cursor=conection.cursor()
        valores = "INSERT INTO ProduccionLech(hora,fecha,cantidad) VALUES(?,?,?)"
        cursor.execute(valores,(hora,fechactual,produccion.text()))
        conection.commit()
        conection.close()
        try:
            QMessageBox.information(Registro, 'Correcto', 'Informacion almacenada correctamente')
            Grafica(tableWidget_3)
            tab.setCurrentIndex(0)
        except Exception as e:
            QMessageBox.information(Registro, 'Error', e)

    else:
        QMessageBox.information(Registro, 'Error', 'Ingrese un valor en el cuadro')

def Grafica(tableWidget_3):
    conection=sqlite3.connect("data/dat")
    sql="SELECT hora,fecha,cantidad FROM ProduccionLech"
    result=conection.execute(sql)
    tableWidget_3.setRowCount(0)

    for row_number,row_data in enumerate(result):
        tableWidget_3.insertRow(row_number)
        for col_number, data in enumerate(row_data):
            tableWidget_3.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))
    conection.close()  
