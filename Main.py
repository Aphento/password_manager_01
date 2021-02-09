import os
from getpass import getpass
from tabulate import tabulate
from conexion import *
import Usuario
from Password import *

conexion = conectar()
crearTablas(conexion)


def inicio():
    os.system("cls")
    comprobar = Usuario.comprobarUsuario()
    if (len(comprobar) == 0):
        print("Bienvenido, registre su informacion.")
        nombre = input("Ingrese su usuario: ")
        master_key = getpass("Ingrese su masterkey: ")
        respuesta = Usuario.registrarUsuario(nombre, master_key)
        if (respuesta == "Registro correcto."):
            print(f"Bienvenido {nombre}")
            menu()
        else:
            print(respuesta)
    else:
        master_key = getpass("Ingrese la masterkey: ")
        respuesta = Usuario.comprobar_datos(1, master_key)
        if (len(respuesta) == 0):
            print("Contraseña incorrecta.")
        else:
            print(f"Bienvenido")
            menu()


def menu():
    while True:
        print("OPCIONES")
        print("\t1. Agregar contraseña")
        print("\t2. Mostrar todas las contraseñas")
        print("\t3. Mostrar contraseña individual")
        print("\t4. Modificar contraseña")
        print("\t5. Borrar contraseña")
        print("\t6. Salir")
        opc = int(input("Digite una opcion: "))

        if opc == 1:
            nueva_password()
        elif opc == 2:
            mostrar_password()
        elif opc == 3:
            buscar_password()
        elif opc == 4:
            modificar_password()
        elif opc == 5:
            eliminar_password()
        elif opc == 6:
            break
        else:
            print("No ingreso una opcion valida.")


def nueva_password():
    website = input("Ingrese el nombre del sitio: ")
    url = input("Ingrese la url: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    description = input("Ingrese la descripción: ")
    respuesta = registrar(website, url, username, password, description)
    print(respuesta)


def mostrar_password():
    datos = mostrar()
    nuevos_datos = []
    headers = ['ID', 'WEBSITE', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION']
    for dato in datos:
        convertir = list(dato)
        convertir[4] = "****"
        nuevos_datos.append(convertir)

    tabla = tabulate(nuevos_datos, headers, tablefmt="fancy_grid")
    print('\t\t\tTodas las contraseñas')
    print(tabla)


def buscar_password():
    master_key = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_datos(1, master_key)

    if (len(respuesta) == 0):
        print("Contraseña incorrecta.")
    else:
        id = int(input("Ingrese el id: "))
        datos = buscar(id)
        headers = [
            'ID', 'WEBSITE', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION'
        ]
        tabla = tabulate(datos, headers, tablefmt="fancy_grid")
        print(tabla)


def modificar_password():
    master_key = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_datos(1, master_key)
    if (len(respuesta) == 0):
        print("Contraseña incorrecta.")
    else:
        id = int(input("Ingrese el id: "))
        website = input("Ingrese el nuevo nombre: ")
        url = input("Ingrese la nueva url: ")
        username = input("Ingrese el nuevo username: ")
        password = input("Ingrese el nuevo password: ")
        description = input("Ingrese la nueva descripción: ")
        respuesta = modificar(id, website, url, username, password,
                              description)
        print(respuesta)


def eliminar_password():
    master_key = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_datos(1, master_key)
    if (len(respuesta) == 0):
        print("Contraseña incorrecta.")
    else:
        id = int(input("Ingrese el id: "))
        respuesta = eliminar(id)
        print(respuesta)


inicio()