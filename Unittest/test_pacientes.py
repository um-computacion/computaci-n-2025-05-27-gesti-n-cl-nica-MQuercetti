import unittest
from src.models.pacientes import Paciente
from src.models.NotFound import DatosInvalidosException


class TestPaciente(unittest.TestCase):
    
    def test_creacion_paciente_exitosa(self):
        
        paciente = Paciente("Gonzalo Rodríguez", "27654321", "14/08/2001")
        self.assertEqual(paciente.obtener_dni(), "27654321")
        self.assertEqual(paciente.obtener_nombre(), "Juan Pérez")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "12/12/2000")
        self.assertEqual(str(paciente), "Juan Pérez, 27654321, 12/12/2000")

    def test_nombre_vacio(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "27654321", "14/08/2001")

    def test_nombre_solo_espacios(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("   ", "27654321", "14/08/2001")

    def test_nombre_con_caracteres_invalidos(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan123", "27654321", "14/08/2001")

    def test_dni_vacio(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "", "14/08/2001")

    def test_dni_muy_corto(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654", "12/12/2000")

    def test_dni_muy_largo(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654321234", "12/12/2000")

    def test_dni_con_letras(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654321", "12/12/2000")

    def test_fecha_vacia(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654321", "")

    def test_fecha_formato_incorrecto(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654321", "2000-12-12")

    def test_fecha_invalida(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "27654321", "32/13/2000")

    def test_dni_diferente(self):
        
        paciente1 = Paciente("Juan Pérez", "27654321", "12/12/2000")
        paciente2 = Paciente("Ana López", "87654321", "01/01/1990")
        self.assertNotEqual(paciente1.obtener_dni(), paciente2.obtener_dni())


if __name__ == "__main__":
    unittest.main()