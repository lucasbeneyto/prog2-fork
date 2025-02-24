class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero, capacidad, recursos):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula

    def mostrar_detalles(self):
        print(f'"Aula Número: {self.numero}\nCapacidad: {self.capacidad} personas\nRecursos: {', '.join(self.recursos)}')

    def reservar_aula(self):
        print(f"El aula {self.numero} ha sido reservada.")

    def __str__(self):
        return f"Aula {self.numero} - Capacidad: {self.capacidad} - Recursos: {', '.join(self.recursos)}"

    def __repr__(self):
        return f"Aula({self.numero}, {self.capacidad}, {self.recursos})"

    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)

    @staticmethod
    def es_adecuada_la_clase(estudiantes, capacidad):
        return estudiantes <= capacidad

