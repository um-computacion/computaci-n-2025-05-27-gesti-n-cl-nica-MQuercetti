import unittest
from datetime import datetime
from src.models.turnos import Turno as turno
from src.models.pacientes import Pacientes_de_Clinica as pacientes
from src.models.medico import Medico
from src.models.especialidad import Especialidad


class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = pacientes("Domingo Hernandez", "64358279", "19/06/2000")
        self.medico = Medico("Dra. Maria Etchegoyen", "4895960")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["jueves"]))
        self.fecha_hora = datetime(2026, 6, 1, 10, 0)
        self.especialidad = "Pediatría"
        self.turno = turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)

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
        self.assertIn("Dr. Maria Etchegoyen", turno_str)
        self.assertIn("Pediatría", turno_str)
        self.assertIn("01/06/2026", turno_str)

    def test_turno_str_format(self):
        turno_str = str(self.turno)
        self.assertTrue(turno_str.startswith("Turno:"))
        self.assertIn(",", turno_str)
        self.assertIn("10:00", turno_str)

    def test_turno_diferentes_pacientes(self):
        paciente2 = pacientes("Ana Perez", "12345678", "01/01/1990")
        turno2 = turno(paciente2, self.medico, self.fecha_hora, self.especialidad)
        self.assertIn("Ana Perez", str(turno2))

    def test_turno_diferentes_especialidades(self):
        especialidad2 = "Cardiología"
        self.medico.agregar_especialidad(Especialidad(especialidad2, ["viernes"]))
        turno2 = turno(self.paciente, self.medico, self.fecha_hora, especialidad2)
        self.assertIn(especialidad2, str(turno2))

    def test_turno_distinta_fecha(self):
        fecha_nueva = datetime(2026, 7, 15, 15, 30)
        turno2 = turno(self.paciente, self.medico, fecha_nueva, self.especialidad)
        self.assertIn("15:30", str(turno2))
        self.assertIn("15/07/2026", str(turno2))

    def test_turno_distinto_medico(self):
        medico2 = Medico("Dr. Juan Perez", "1234567")
        medico2.agregar_especialidad(Especialidad("Pediatría", ["jueves"]))
        turno2 = turno(self.paciente, medico2, self.fecha_hora, self.especialidad)
        self.assertIn("Dr. Juan Perez", str(turno2))

    def test_turno_repr(self):
        turno_repr = repr(self.turno)
        self.assertIn("Turno", turno_repr)
        self.assertIn("Domingo Hernandez", turno_repr)

    def test_turno_igualdad(self):
        turno2 = turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)
        self.assertEqual(self.turno, turno2)

    def test_turno_distinta_especialidad(self):
        especialidad2 = "Dermatología"
        self.medico.agregar_especialidad(Especialidad(especialidad2, ["lunes"]))
        turno2 = turno(self.paciente, self.medico, self.fecha_hora, especialidad2)
        self.assertIn("Dermatología", str(turno2))


if __name__ == "__main__":
    unittest.main()

    def test_obtener_paciente(self):
        self.assertEqual(self.turno.obtener_paciente(), self.paciente)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_obtener_especialidad(self):
        self.assertEqual(self.turno.obtener_especialidad(), self.especialidad)

    def test_str(self):
        turno_str = str(self.turno)
        self.assertIn("Domingo Hernandez", turno_str)
        self.assertIn("Dra. Maria Etchegoyen", turno_str)  
        self.assertIn("Pediatría", turno_str)
        self.assertIn("01/06/2026", turno_str)  

    def test_turno_str_format(self):
        turno_str = str(self.turno)
        self.assertTrue(turno_str.startswith("Turno:"))
        self.assertIn(",", turno_str)
        self.assertIn("10:00", turno_str)

    def test_turno_diferentes_pacientes(self):
        paciente2 = pacientes("Domingo Hernandez", "12345678", "01/01/1990")
        turno2 = turno(paciente2, self.medico, self.fecha_hora, self.especialidad)
        self.assertIn("Domingo Hernandez", str(turno2))

    def test_turno_diferentes_especialidades(self):
        especialidad2 = "Cardiología"
        self.medico.agregar_especialidad(Especialidad(especialidad2, ["viernes"]))
        turno2 = turno(self.paciente, self.medico, self.fecha_hora, especialidad2)
        self.assertIn(especialidad2, str(turno2))

    def test_turno_distinta_fecha(self):
        fecha_nueva = datetime(2026, 7, 15, 15, 30)
        turno2 = turno(self.paciente, self.medico, fecha_nueva, self.especialidad)
        self.assertIn("10:00", str(turno2))
        self.assertIn("01/06/2026", str(turno2))


if __name__ == "__main__":
    unittest.main()

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