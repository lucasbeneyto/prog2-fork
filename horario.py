class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario

    def mostrar_horario(self):
        print(f'Hora inicio: {self.hora_inicio} | Hora final: {self.hora_fin} | Curso: {self.curso} | Día: {self.dia}')

    def modificar_horario(self, nuevo_horario: dict):
        if 'curso' in nuevo_horario:
            self.curso = nuevo_horario['curso']
        if 'dia' in nuevo_horario:
            self.dia = nuevo_horario['dia']
        if 'hora_inicio' in nuevo_horario:
            self.hora_inicio = nuevo_horario['hora_inicio']
        if 'hora_fin' in nuevo_horario:
            self.hora_fin = nuevo_horario['hora_fin']

    def __str__(self):
        return (
            f"Horario de {self.curso} "
            f"el día {self.dia}"
            f"de {self.hora_inicio} hasta {self.hora_fin}"
        )

    def __repr__(self):
        return (
            f"Horario(curso={repr(self.curso)}, dia={repr(self.dia)}, "
            f"hora_inicio={repr(self.hora_inicio)}, hora_fin={repr(self.hora_fin)})"
        )

    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)

    @staticmethod
    def es_horario_valido(hora_inicio, hora_fin):
        return hora_inicio < hora_fin