import os
import time


def isdigit(argumento):
    while True:
        if argumento.isdigit():
            argumento = int(argumento)
            break
        else:

            print('No es valido.')
            continue
    return argumento


def menu_principal():
    os.system('cls')
    print('Menu Principal'.center(50, ' '))
    print('1.- Registrarte. ')
    print('2.- Iniciar sesión.')
    print('3.- Salir.')
    while True:
        respuesta = input('Ingresa a respuesta por el numero:\n')
        respuesta = isdigit(respuesta)
        if respuesta <= 3:
            break
        else:
            print('No es valido.')
            time.sleep(1)
            continue
    return respuesta


def menu_registro():
    print('Menu de Registro.'.center(50, ' '))
    print('1.- Alumno\n2.- Profesor\n3.- Salir.')
    while True:
        respuesta = input('Ingresa a respuesta por el numero:\n')
        respuesta = isdigit(respuesta)
        if respuesta <= 3:
            break
        else:
            print('No es valido.')
            time.sleep(1)
            continue
    return respuesta


def inicio_ses():
    print('Inicio de sesion.'.center(50, ' '))
    clave = input('Ingresa tu clave:\n').upper()
    return clave


def menu_profesor(nombre):
    print(('Bienvenido Profesor ' + nombre).center(50, ' '))
    print('1.-Crear clase.\n2.-Dar de Baja Clase\n3.-Agregar Calificacion\n4.-Revisar horario.\n5.-Ver informacion '
          'personal\n6.-Regresar')
    while True:
        respuesta = input('Ingresa a respuesta por el numero:\n')
        respuesta = isdigit(respuesta)
        if respuesta <= 6:
            break
        else:
            print('No es valido.')
            time.sleep(1)
            continue
    return respuesta


def menu_dar_baja():
    print('Baja de Clase'.center(50, ' '))
    nombre = input('Ingresa el nombre de la clase:\n')
    return nombre

