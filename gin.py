#!/usr/bin/python3
import mysql.connector #Importamos la libreria mysql para realizar la conexion
from mysql.connector import errorcode
import cgi

data = cgi.FieldStorage()

#Declaramos la variables, en las cuales se almacenara los datos de las cajas del html
usuario = data.getvalue('usuario')
ide = data.getvalue('id')
descripcion = data.getvalue('des')
especificacion = data.getvalue('espe')
precio = data.getvalue('precio')
cantidad = data.getvalue('can')

try:
  cnx = mysql.connector.connect(user='Nices', password = 'Nices123*', database='Tienda', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cur = cnx.cursor()
    print('content-type: text/html')
    print('')
    sql = ("insert into Productos values ('{}', '{}', '{}', '{}', '{}', '{}')".format(usuario, ide, descripcion, especificacion, precio, cantidad))
    cur.execute(sql)
    cnx.commit()
    print('<script> location.href="/ProyectoArquitectura/index.html";</script>')
cnx.close()
