import hashlib
from conexion import *


def comprobarUsuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = "SELECT * FROM users"
    cursor.execute(sentencia_sql)
    usuarioValido = cursor.fetchall()
    conexion.close()
    return usuarioValido


def registrarUsuario(username, master_key):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = "INSERT INTO users (username, master_key) VALUES (?,?)"
        ps_cif = hashlib.sha256(master_key.encode('utf-8')).hexdigest()
        datos = (username, ps_cif)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return "Registro correcto."
    except Error as err:
        return f"Ha ocurrido un error. {str(err)}"


def comprobar_datos(id, master_key):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = """SELECT * FROM users WHERE id=? AND master_key=?"""
        ps_cif = hashlib.sha256(master_key.encode('utf-8')).hexdigest()
        cursor.execute(sentencia_sql, (id, ps_cif))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        return f"Ha ocurrido un error {str(err)}"
