from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad] = None):
        if not nombre or not matricula:
            raise ValueError("Nombre y matrícula son obligatorios.")
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades or []

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str):
        for e in self.__especialidades:
            if e.verificar_dia(dia):
                return e.obtener_especialidad()
        return None

    def __str__(self):
        esp = ", ".join([str(e) for e in self.__especialidades])
        return f"{self.__nombre}, {self.__matricula}, [{esp}]"
