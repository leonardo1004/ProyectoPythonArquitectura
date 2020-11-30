#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

data = cgi.FieldStorage()

usuario = data.getvalue('usuario')
contra = data.getvalue('password')

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
    sql = ("insert into Personas  values ('{}', SHA('{}'))".format(usuario, contra))
    cur.execute(sql)
    cnx.commit()
    print('<script> location.href="/ProyectoArquitectura/index.html";</script>')
cnx.close()
