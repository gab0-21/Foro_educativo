
class Alumno(Usuario):
    def __init__(self, nombre, contraseña, edad, sexo, matricula):
        super().__init__(nombre, contraseña, edad, sexo)
        self._matricula = matricula

    # Método getter específico para la matrícula
    def obtener_matricula(self):
        return self._matricula

    # Métodos adicionales para el alumno
    def consultar_horario(self):
        print("Horario consultado por el alumno", self.obtener_nombre())

    def consultar_calificaciones(self):
        print("Calificaciones consultadas por el alumno", self.obtener_nombre())

    def cerrar_sesion(self):
        print("Sesión cerrada para el alumno", self.obtener_nombre())
