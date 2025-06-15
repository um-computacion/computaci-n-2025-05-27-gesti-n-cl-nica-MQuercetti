import unittest
from src.models.pacientes import Pacientes_de_Clinica as Paciente
from src.models.NotFound import DatosInvalidosException


class TestPaciente(unittest.TestCase):
    
    def test_creacion_paciente_exitosa(self):
        
        paciente = Paciente("Gonzalo Rodríguez", "27654321", "14/08/2001")
        self.assertEqual(paciente.obtener_dni(), "27654321")
        self.assertEqual(paciente.obtener_nombre(), "Gonzalo Rodríguez")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "14/08/2001")
        self.assertEqual(str(paciente), "Gonzalo Rodríguez, 27654321, 14/08/2001")

    def test_nombre_vacio(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "27654321", "14/08/2001")

    def test_nombre_solo_espacios(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("   ", "27654321", "14/08/2001")

    def test_nombre_con_caracteres_invalidos(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez@!#", "27654321", "14/08/2001")

    def test_dni_vacio(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "", "14/08/2001")

    def test_dni_muy_corto(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654", "14/08/2001")

    def test_dni_muy_largo(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654321234", "14/08/2001")

    def test_dni_con_letras(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654321aSdq", "14/08/2001")

    def test_fecha_vacia(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654321", "")

    def test_fecha_formato_incorrecto(self):
       
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654321", "2014-08-14")

    def test_fecha_invalida(self):
        
        with self.assertRaises(DatosInvalidosException):
            Paciente("Gonzalo Rodríguez", "27654321", "57/14/1500")

    def test_dni_diferente(self):
        
        paciente1 = Paciente("Gonzalo Rodríguez", "27654321", "14/08/2001")
        paciente2 = Paciente("Maria Barbosa", "74518234", "19/11/1970")
        self.assertNotEqual(paciente1.obtener_dni(), paciente2.obtener_dni())


if __name__ == "__main__":
    unittest.main()