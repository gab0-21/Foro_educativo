import Menu
import alumnos
import Profesor
import pickle
import clases


def main():
    with open('base_datos.pickle', "rb") as archivo:
        base_de_datos = pickle.load(archivo)
    # base_de_datos = {'Administrador': Profesor.Profesor('Admin', 'Admin', '1', 'xw', 'xw')}
    while True:
        respuesta = Menu.menu_principal()
        if respuesta == 1:
            respuesta_2 = Menu.menu_registro()
            if respuesta_2 == 1:
                resp1, resp2, resp3, resp4, resp5 = alumnos.preguntas_agre()
                alumno_1 = alumnos.Alumno(resp1, resp2, resp3, resp4, resp5)
                base_de_datos[alumno_1.get_nombre()] = alumno_1
                print('Se ha regitrado exitosamente al Alumno.\nTu ID es:')
                print(alumno_1.get_id())
            elif respuesta_2 == 2:
                resp1, resp2, resp3, resp4, resp5 = Profesor.preguntas_agre()
                profesor_1 = Profesor.Profesor(resp1, resp2, resp3, resp4, resp5)
                base_de_datos[profesor_1.get_nombre()] = profesor_1
                print('Se ha regitrado exitosamente al Profesor.\nTu ID es:')
                print(profesor_1.get_id())
            else:
                print('¿Seguro quieres salir?'.capitalize())
                respuesta_3 = input('Si/No').upper()
                if respuesta_3 == 'SI':
                    with open('base_datos.pickle', "wb") as archivo:
                        pickle.dump(base_de_datos, archivo)
                    break
                else:
                    continue
        elif respuesta == 2:
            clave = Menu.inicio_ses()
            for objeto in base_de_datos.values():
                # Verificar si el ID coincide
                if objeto.get_id() == clave:
                    if objeto.get_id()[-4:] == "P0F3":  # verificacion de profesor
                        while True:
                            respuesta_4 = Menu.menu_profesor(objeto.get_nombre())
                            if respuesta_4 == 1:
                                resp1, resp2, resp3, resp4 = clases.preguntas_agre(objeto.get_nombre())
                                clase_1 = clases.Clase(resp1, resp2, resp3, resp4)
                                objeto.agregar_clase(clase_1)
                            elif respuesta_4 == 2:
                                nombre = Menu.menu_dar_baja()
                                objeto.eliminar_clase(nombre)
                            elif respuesta_4 == 3:
                                print('Aun no tenemos esta funcion.')
                            elif respuesta_4 == 4:
                                objeto.get_horarios()
                            elif respuesta_4 == 5:
                                objeto.mostrar_datos_usuario()
                            else:
                                print('¿Seguro quieres salir?'.capitalize())
                                respuesta_3 = input('Si/No').upper()
                                if respuesta_3 == 'SI':
                                    break
                                else:
                                    continue
                    else:
                        print('Menu Alumno (aun no esta disponible)')
                    break
            else:
                print("El ID {} no se encontró en el diccionario de objetos.".format(clave))

        else:
            print('¿Seguro quieres salir?'.capitalize())
            respuesta_3 = input('Si/No\n').upper()
            if respuesta_3 == 'SI':
                with open('base_datos.pickle', "wb") as archivo:
                    pickle.dump(base_de_datos, archivo)
                break
            else:
                continue


main()
