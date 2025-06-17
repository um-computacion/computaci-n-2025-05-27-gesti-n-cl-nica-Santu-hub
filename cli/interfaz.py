from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime
from modelo.excepciones import *


class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def iniciar(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")
            opcion = input("Elegí una opción: ")

            try:
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia()
                elif opcion == "7":
                    self.ver_turnos()
                elif opcion == "8":
                    self.ver_pacientes()
                elif opcion == "9":
                    self.ver_medicos()
                elif opcion == "0":
                    break
            except Exception as e:
                print("Error:", str(e))

    def agregar_paciente(self):
        nombre = input("Nombre del paciente: ")
        dni = input("DNI: ")
        fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha_nac)
        self.clinica.agregar_paciente(paciente)
        print("Paciente agregado correctamente.")

    def agregar_medico(self):
        nombre = input("Nombre del médico: ")
        matricula = input("Matrícula profesional: ")
        medico = Medico(nombre, matricula)
        self.clinica.agregar_medico(medico)
        print("Médico agregado correctamente.")

    def agendar_turno(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        fecha_str = input("Fecha y hora del turno (aaaa-mm-dd HH:MM): ")
        fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
        print("Turno agendado correctamente.")

    def agregar_especialidad(self):
        matricula = input("Matrícula del médico: ")
        medico = self.clinica.obtener_medico_por_matricula(matricula)
        tipo = input("Nombre de la especialidad: ")
        dias = input("Días de atención (separados por coma): ").split(',')
        especialidad = Especialidad(tipo.strip(), [d.strip().lower() for d in dias])
        medico.agregar_especialidad(especialidad)
        print("Especialidad agregada al médico.")

    def emitir_receta(self):
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos = input("Medicamentos (separados por coma): ").split(',')
        self.clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
        print("Receta emitida correctamente.")

    def ver_historia(self):
        dni = input("DNI del paciente: ")
        historia = self.clinica.obtener_historia_clinica(dni)
        print(historia)

    def ver_turnos(self):
        for turno in self.clinica.obtener_turnos():
            print(turno)

    def ver_pacientes(self):
        for paciente in self.clinica.obtener_pacientes():
            print(paciente)

    def ver_medicos(self):
        for medico in self.clinica.obtener_medicos():
            print(medico)
