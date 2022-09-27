#!C:/Python310/python.exe
# Librerias para conexion con MySQL y Servidor Apache
import mysql.connector
import os
import cgi
import cgitb

cgitb.enable()

# Toda pagina web inicia con el tipo de contenido y una linea en blanco
print("Content-type: text/html")
print()

# Se revisa el tipo de peticion http GET, POST, PUT, DELETE
metodo = os.environ["REQUEST_METHOD"]

# Se obtiene una lista de valores recibidos del formulario 
valoresUrl = cgi.FieldStorage()

if metodo == 'GET':
    print("Metodo de consulta")
    print()
    query = ("SELECT * FROM topics")
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    for (id, title, user_id) in cursor:
        print("id:%s, title:%s, user_id:%s" % (id, title, user_id))
    cursor.close()
elif metodo == 'POST':
    print("Metodo de agregar")
    print()
elif metodo == 'PUT':
    print("Metodo de actualizar")
    print()
elif metodo == 'DELETE':
    print("Metodo de eliminar")
    print()
else:
    print("Error")
    print()
