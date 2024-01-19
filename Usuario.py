class Usuario:
    def __init__(self, nombre, contraseña, edad, sexo):
        self._nombre = nombre
        self._contraseña = contraseña
        self._edad = edad
        self._sexo = sexo

    # Métodos getter
    def obtener_nombre(self):
        return self._nombre

    def obtener_contraseña(self):
        return self._contraseña

    def obtener_edad(self):
        return self._edad

    def obtener_sexo(self):
        return self._sexo
