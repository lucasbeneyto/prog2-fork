class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante

    def inscribir_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            print(f"{self.nombre} ha sido inscrito en el curso: {curso}")
        else:
            print(f"{self.nombre} ya está inscrito en el curso: {curso}")

    def mostrar_informacion(self):
        cursos = ", ".join(self.cursos_inscritos) if self.cursos_inscritos else "Ninguno"
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCursos inscritos: {cursos}")

    def __str__(self):
        return f"Estudiante({self.nombre}, {self.edad} años, Cursos: {self.cursos_inscritos})"

    def __repr__(self):
        return f"Estudiante('{self.nombre}', {self.edad}, {self.cursos_inscritos})"

    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18
