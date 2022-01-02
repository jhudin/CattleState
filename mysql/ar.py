import mysql.connector
dato = {
            'user': 'informacion_db',
            'password': '123456789',
            'database': 'informaciondb',
            'host': 'db4free.net',
        }
try:
    conexion = mysql.connector.connect(**dato)
    cursor = conexion.cursor()
    sql = "CREATE TABLE Ranimales(codigo int (11),nombre varchar (50),fnacimiento varchar (50),mingreso varchar (50),fingreso varchar (50),raza varchar (50),sexo varchar (50),lote varchar (50),crias int (11),peso varchar (50),procedencia varchar (50),estado varchar (50),salud varchar (50),hregistro varchar (50),produccion varchar (50),color varchar (50),rutfot varchar (150))"
    cursor.execute(sql)
except Exception as e:
    print(e)