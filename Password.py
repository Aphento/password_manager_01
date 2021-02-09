from conexion import *


def registrar(nombre, url, username, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO passwords(
      website, url, username, password, description) 
      VALUES (?, ?, ?, ?, ?)'''
        datos = (nombre, url, username, contrasena, descripcion)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return "Registro correcto."
    except Error as err:
        return f"Ha sucedido un error {str(err)}"


def mostrar():
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM passwords'''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return f"Ha ocurrido un error {str(err)}"
    return datos


def buscar(id):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM passwords WHERE id=?'''
        cursor.execute(sentencia_sql, (id, ))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return f"Ha ocurrido un error {str(err)}"
    return datos


def modificar(id, nombre, url, username, contrasena, description):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE passwords SET website=?, url=?, username=?, password=?, description=? WHERE id=?'''
        datos = (nombre, url, username, contrasena, description, id)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return "Se modifico correctamente."
    except Error as err:
        return f"Ha ocurrido un error {str(err)}"


def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = "DELETE FROM passwords WHERE id=?"
        cursor.execute(sentencia_sql, (id, ))
        conexion.commit()
        conexion.close()
        return "Se elimino correctamente."
    except Error as err:
        return f"Ha ocurrido un error {str(err)}"
