class Profesor:
    total_profesores = 0  # Contador de instancias

    def __init__(self, nombre, especialidad, cursos_asignados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1  # Aumenta el contador cada vez que se crea un profesor
    def prueba ():
        pass    