class Profesor(Usuario):
    def __init__(self, nombre, contraseña, edad, sexo, especialidad):
        super().__init__(nombre, contraseña, edad, sexo)
        self._especialidad = especialidad

    # Método getter específico para la especialidad
    def obtener_especialidad(self):
        return self._especialidad

    # Métodos adicionales para el profesor
    def crear_clase(self):
        print("Clase creada por el profesor", self.obtener_nombre())

    def cerrar_sesion(self):
        print("Sesión cerrada para el profesor", self.obtener_nombre())
