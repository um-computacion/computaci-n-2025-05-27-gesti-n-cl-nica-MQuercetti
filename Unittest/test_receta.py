import unittest
from src.models.receta import Receta
from src.models.pacientes import Pacientes_de_Clinica as Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad


class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Gonzalo Rodríguez", "27654321", "14/08/2001")
        self.medico = Medico("Dra. Maria Etchegoyen", "48900126")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))
        
        self.medicamentos = ["Alcohol etilico", "Acnoxin"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_obtener_paciente(self):
        self.assertEqual(self.receta.obtener_paciente(), self.paciente)

    def test_obtener_medico(self):
        self.assertEqual(self.receta.obtener_medico(), self.medico)

    def test_obtener_medicamentos(self):
        medicamentos = self.receta.obtener_medicamentos()
        self.assertEqual(medicamentos, ["Alcohol etilico", "Acnoxin"])

    def test_obtener_fecha(self):
        fecha = self.receta.obtener_fecha()
        self.assertIsNotNone(fecha)

    def test_str(self):
        receta_str = str(self.receta)
        self.assertIn("Gonzalo Rodríguez", receta_str)
        self.assertIn("Dra. Maria Etchegoyen", receta_str)
        self.assertIn("Acnoxin", receta_str)
        self.assertIn("Alcohol etilico", receta_str)


if __name__ == "__main__":
    unittest.main()