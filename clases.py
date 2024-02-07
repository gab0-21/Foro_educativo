def preguntas_agre(nombre_profe):
    print('Crear clase'.center(50, ' '))
    class_name = input("Ingrese el nombre de la clase: \n")
    class_hour = input("Ingrese el horario de la clase (en este formato: inicio - fin): \n")
    clase_code = input("Ingrese el codigo de zoom de la clase: \n")
    return class_name, nombre_profe, class_hour, clase_code


class Clase:
    def __init__(self, nombre, profesor, horario, codigo):
        self.__nombre = nombre.upper()
        self.__profesor = profesor.upper()
        self.__horario = horario
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def get_profesor(self):
        return self.__profesor

    def get_horario(self):
        return self.__horario

    def get_codigo(self):
        return self.__codigo
    