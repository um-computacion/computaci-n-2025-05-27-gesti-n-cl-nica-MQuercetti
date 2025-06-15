import unittest
from src.models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def setUp(self):
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "jueves"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.especialidad.obtener_especialidad(), "Pediatría")

    def test_verificar_dia(self):
        self.assertTrue(self.especialidad.verificar_dia("lunes"))
        self.assertTrue(self.especialidad.verificar_dia("Miércoles"))
        self.assertFalse(self.especialidad.verificar_dia("viernes"))

    def test_str(self):
        self.assertIn("Pediatría", str(self.especialidad))
        self.assertIn("lunes", str(self.especialidad))

if __name__ == "__main__":
    unittest.main()