import unittest
from datetime import datetime
from src.models.turnos import turnos
from src.models.pacientes import pacientes
from src.models.medico import Medico
from src.models.especialidad import Especialidad


class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = pacientes ("Domingo Hernandez", "64358279", "19/06/2000")
        self.medico = Medico("Dr. Carlos Gómez", "489")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["miercoles"]))
        
        self.fecha_hora = datetime(2026, 6, 1, 10, 0)
        self.especialidad = "Pediatría"
        self.turno = turnos(self.paciente, self.medico, self.fecha_hora, self.especialidad)

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_paciente(self):
        self.assertEqual(self.turno.obtener_paciente(), self.paciente)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_obtener_especialidad(self):
        self.assertEqual(self.turno.obtener_especialidad(), self.especialidad)

    def test_str(self):
        turno_str = str(self.turno)
        self.assertIn("Domingo Hernandez", turno_str)
        self.assertIn("Dra. Maria Etchegoyen ", turno_str)
        self.assertIn("Pediatría", turno_str)
        self.assertIn("10/08/2002", turno_str)


if __name__ == "__main__":
    unittest.main()