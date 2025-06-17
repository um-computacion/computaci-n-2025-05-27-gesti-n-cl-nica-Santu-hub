class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not dias:
            raise ValueError("Especialidad debe tener nombre y días válidos.")
        self.__tipo = tipo
        self.__dias = [dia.lower() for dia in dias]

    def obtener_especialidad(self):
        return self.__tipo

    def verificar_dia(self, dia: str):
        return dia.lower() in self.__dias

    def __str__(self):
        dias = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias})"