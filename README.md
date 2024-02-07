# Foro_educativo
Proyecto de fundamentos de ingenieria de software 

Manual de Usuario - Sistema de Gestión Académica
Descripción
Este sistema de gestión académica permite registrar alumnos y profesores, así como realizar operaciones específicas dependiendo del tipo de usuario. Los datos se almacenan en un archivo de base de datos utilizando el formato pickle para persistencia.

Inicio
Ejecutar el programa main.py para iniciar el sistema.

Se cargará la base de datos existente, si la hay, o se creará una nueva.

Se mostrará un menú principal con las siguientes opciones:

Registro: Permite registrar un nuevo alumno o profesor.
Inicio de Sesión: Permite iniciar sesión como alumno o profesor para acceder a funciones específicas.
Salir: Permite salir del sistema.
Registro
Selecciona la opción "Registro" en el menú principal.
Selecciona el tipo de usuario que deseas registrar: alumno o profesor.
Completa los datos solicitados para el registro.
Se generará un ID único para el usuario registrado.
El usuario se añadirá a la base de datos y se mostrará el ID asignado.
Inicio de Sesión
Selecciona la opción "Inicio de Sesión" en el menú principal.
Ingresa el ID correspondiente al usuario que deseas iniciar sesión.

Si el ID es válido, se mostrará un menú con funciones específicas según el tipo de usuario:

Profesor: Permite gestionar clases, ver horarios y datos del usuario.
Alumno: (Funcionalidad aún no disponible).
Funciones del Profesor
Agregar Clase: Permite agregar una nueva clase al horario del profesor.
Eliminar Clase: Permite eliminar una clase del horario del profesor.
Consultar Horarios: Muestra el horario de clases del profesor.
Ver Datos de Usuario: Muestra los datos personales del profesor.
Salir: Permite salir del menú de funciones del profesor y volver al menú principal.
Salida del Sistema
En cualquier momento, puedes seleccionar la opción "Salir" en el menú principal o en los menús de funciones.
Se te pedirá confirmación antes de salir.
Si confirmas, se guardarán los cambios en la base de datos y se cerrará el programa.
¡Listo! Ahora puedes utilizar el sistema de gestión académica para registrar usuarios, gestionar clases y ver información personal. Si necesitas ayuda adicional, consulta la documentación o contacta al administrador del sistema.
