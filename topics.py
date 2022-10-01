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
    conexion.close()
elif metodo == 'POST':
    print("Metodo de agregar")
    print()
    titulo = valoresUrl["title"].value
    uid = valoresUrl["user_id"].value
    query = ("INSERT INTO topics(title, user_id) VALUES('{}', {})".format(titulo, uid))
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    print("Se agrego %s registro" % cursor.rowcount)
    cursor.close()
    conexion.close()
elif metodo == 'PUT':
    print("Metodo de actualizar")
    print()
    titulo = valoresUrl["title"].value
    uid = valoresUrl["user_id"].value
    id = valoresUrl["id"].value
    query = (
        "UPDATE topics SET title = '{}', user_id={} WHERE id = {}".format(titulo, uid, id))
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    print("Se modifico %s registro" % cursor.rowcount)
    cursor.close()
    conexion.close()
elif metodo == 'DELETE':
    print("Metodo de eliminar")
    print()
    id = valoresUrl["id"].value
    query = (
        "DELETE FROM topics WHERE id = {}".format(id))
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='foro')
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    print("Se elimino %s registro" % cursor.rowcount)
    cursor.close()
    conexion.close()
else:
    print("Error")
    print()
