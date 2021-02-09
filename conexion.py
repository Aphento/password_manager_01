import sqlite3
from sqlite3 import Error


def conectar():
    try:
        conexion = sqlite3.connect("database.db")
        return conexion
    except Errror as err:
        print("Ha ocurrido un error")


def crearTablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql1 = """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  master_key TEXT NOT NULL)"""
    sentencia_sql2 = """CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT NOT NULL,
    url TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    description TEXT)"""

    cursor.execute(sentencia_sql1)
    cursor.execute(sentencia_sql2)
    conexion.commit()
    conexion.close()
