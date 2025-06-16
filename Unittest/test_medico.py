import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dra. Maria Etchegoyen", "48900126")
        self.especialidad1 = Especialidad("Pediatría", ["lunes", "miércoles", "jueves"])
        self.especialidad2 = Especialidad("Podologia", ["martes", "viernes"])

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("miércoles"), "Pediatría")
        self.medico.agregar_especialidad(self.especialidad2)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("viernes"), "Podologia")

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "48900126")

    def test_str(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertIn("Pediatría", str(self.medico))

if __name__ == "__main__":
    unittest.main()