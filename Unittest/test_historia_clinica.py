import unittest
from unittest.mock import Mock
from src.models.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Mock()
        self.paciente.__str__ = Mock(return_value="Paciente Test")
        self.turno = Mock()
        self.turno.__str__ = Mock(return_value="Turno Test")
        self.receta = Mock()
        self.receta.__str__ = Mock(return_value="Receta Test")
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        self.assertIn(self.turno, self.historia.obtener_turnos())

    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        self.assertIn(self.receta, self.historia.obtener_recetas())

    def test_str(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        self.assertIn("Turno Test", str(self.historia))
        self.assertIn("Receta Test", str(self.historia))

if __name__ == "__main__":
    unittest.main()