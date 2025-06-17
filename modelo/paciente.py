class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Todos los campos del paciente son obligatorios.")
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"
