import unittest
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica
from modelo.turno import Turno
from modelo.clinica import Clinica
from datetime import datetime, timedelta
from modelo.excepciones import *

def test_paciente_valido(self):
    p = Paciente("Ana", "123", "01/01/2000")
    self.assertEqual(p.obtener_dni(), "123")

def test_paciente_datos_invalidos(self):
        with self.assertRaises(ValueError):
            Paciente("", "", "")

def test_medico_y_especialidad(self):
        esp = Especialidad("Cardiología", ["lunes"])
        m = Medico("Dr. Casa", "ABC123")
        m.agregar_especialidad(esp)
        self.assertEqual(m.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(m.obtener_especialidad_para_dia("viernes"))

def test_receta_valida(self):
        p = Paciente("Ana", "123", "01/01/2000")
        m = Medico("Dr. A", "M1")
        r = Receta(p, m, ["Paracetamol"])
        self.assertIn("Paracetamol", str(r))

def test_receta_invalida(self):
        p = Paciente("Ana", "123", "01/01/2000")
        m = Medico("Dr. A", "M1")
        with self.assertRaises(ValueError):
            Receta(p, m, [])

def test_historia_clinica(self):
        p = Paciente("Ana", "123", "01/01/2000")
        hc = HistoriaClinica(p)
        m = Medico("Dr. A", "M1")
        t = Turno(p, m, datetime.now(), "Clínica")
        hc.agregar_turno(t)
        hc.agregar_receta(Receta(p, m, ["Ibuprofeno"]))
        self.assertEqual(len(hc.obtener_turnos()), 1)
        self.assertEqual(len(hc.obtener_recetas()), 1)

def test_clinica_turno_ok(self):
        c = Clinica()
        p = Paciente("Ana", "123", "01/01/2000")
        m = Medico("Dr. A", "M1")
        esp = Especialidad("Clínica", ["lunes"])
        m.agregar_especialidad(esp)
        c.agregar_paciente(p)
        c.agregar_medico(m)
        fecha = datetime.now() + timedelta(days=(7 - datetime.now().weekday()))
        c.agendar_turno("123", "M1", "Clínica", fecha)
        self.assertEqual(len(c.obtener_turnos()), 1)

def test_clinica_turno_error(self):
        c = Clinica()
        with self.assertRaises(PacienteNoEncontradoException):
            c.agendar_turno("999", "M1", "Clínica", datetime.now())

if __name__ == '__main__':
    unittest.main()
