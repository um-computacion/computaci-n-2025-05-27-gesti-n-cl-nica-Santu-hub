from modelo.excepciones import *
from modelo.historia_clinica import HistoriaClinica
from modelo.turno import Turno
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    def agregar_paciente(self, paciente):
        if paciente.obtener_dni() in self.__pacientes:
            raise ValueError("El paciente ya está registrado.")
        self.__pacientes[paciente.obtener_dni()] = paciente
        self.__historias_clinicas[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        if medico.obtener_matricula() in self.__medicos:
            raise ValueError("El médico ya está registrado.")
        self.__medicos[medico.obtener_matricula()] = medico

    def obtener_medico_por_matricula(self, matricula):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException()
        return self.__medicos[matricula]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        dia = self.obtener_dia_semana_en_espanol(fecha_hora)
        medico = self.obtener_medico_por_matricula(matricula)

        self.validar_especialidad_en_dia(medico, especialidad, dia)

        turno = Turno(self.__pacientes[dni], medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if not medicamentos:
            raise RecetaInvalidaException()
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        receta = receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_dia_semana_en_espanol(self, fecha_hora):
        return fecha_hora.strftime('%A').lower()

    def validar_existencia_paciente(self, dni):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()

    def validar_existencia_medico(self, matricula):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException()

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        for turno in self.__turnos:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException()

    def validar_especialidad_en_dia(self, medico, especialidad, dia):
        esp = medico.obtener_especialidad_para_dia(dia)
        if esp != especialidad:
            raise MedicoNoDisponibleException()

    def obtener_historia_clinica(self, dni):
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    def obtener_pacientes(self):
        return list(self.__pacientes.values())

    def obtener_medicos(self):
        return list(self.__medicos.values())

    def obtener_turnos(self):
        return list(self.__turnos)