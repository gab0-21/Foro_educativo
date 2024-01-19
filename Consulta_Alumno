class ConsultaAlumno:
    def __init__(self, alumno, horario=None, calificaciones=None):
        self._alumno = alumno
        self._horario = horario or []
        self._calificaciones = calificaciones or {}

    # Métodos getter
    def obtener_alumno(self):
        return self._alumno

    def obtener_horario(self):
        return self._horario

    def obtener_calificaciones(self):
        return self._calificaciones

    # Métodos relacionados con la consulta de información
    def mostrar_horarios(self):
        print(f"Horario de {self._alumno.obtener_nombre()}: {self._horario}")

    def mostrar_calificaciones(self):
        print(f"Calificaciones de {self._alumno.obtener_nombre()}: {self._calificaciones}")

# Ejemplo de uso
alumno_consulta = Alumno(nombre="EstudianteC", contraseña="clave789", edad=22, sexo="Masculino", matricula="2024003")

# Crear instancia de ConsultaAlumno
consulta_alumno = ConsultaAlumno(alumno=alumno_consulta, horario=["Lunes 14:00-16:00", "Miércoles 15:00-17:00"], calificaciones={"examen1": 95, "examen2": 88})

