from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        if not medicamentos:
            raise ValueError("La receta debe contener medicamentos.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        meds = ", ".join(self.__medicamentos)
        return f"Receta({self.__paciente}, {self.__medico}, [{meds}], {self.__fecha})"