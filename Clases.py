class Clase:
    def __init__(self, materia, horarios, cupos, profesor):
        self._materia = materia
        self._horarios = horarios
        self._cupos = cupos
        self._profesor = profesor
        self._alumnos_inscritos = {}  # Diccionario para almacenar información de los alumnos inscritos

    # Métodos getter
    def obtener_materia(self):
        return self._materia

    def obtener_horarios(self):
        return self._horarios

    def obtener_cupos_disponibles(self):
        return self._cupos - len(self._alumnos_inscritos)

    def obtener_profesor(self):
        return self._profesor

    # Métodos relacionados con los alumnos
    def consultar_alumnos(self):
        return list(self._alumnos_inscritos.keys())

    def dar_alta_alumno(self, alumno):
        if len(self._alumnos_inscritos) < self._cupos:
            self._alumnos_inscritos[alumno.obtener_nombre()] = alumno
            print(f"Alumno {alumno.obtener_nombre()} inscrito en la clase de {self._materia}")
        else:
            print("No hay cupos disponibles para la clase.")

    def dar_baja_alumno(self, alumno):
        if alumno.obtener_nombre() in self._alumnos_inscritos:
            del self._alumnos_inscritos[alumno.obtener_nombre()]
            print(f"Alumno {alumno.obtener_nombre()} dado de baja de la clase de {self._materia}")
        else:
            print("El alumno no está inscrito en la clase.")

    # Otros métodos
    def consultar_horarios(self):
        print(f"Horarios de la clase de {self._materia}: {self._horarios}")

    def modificar_calificaciones(self, alumno, calificaciones):
        if alumno.obtener_nombre() in self._alumnos_inscritos:
            # Supongamos que calificaciones es un diccionario con las nuevas calificaciones
            # Este método podría ser más complejo dependiendo de la lógica real de tu aplicación
            # Aquí simplemente lo mostramos como ejemplo
            print(f"Calificaciones modificadas para el alumno {alumno.obtener_nombre()}: {calificaciones}")
        else:
            print("El alumno no está inscrito en la clase.")
