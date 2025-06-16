import unittest
from datetime import datetime, timedelta
from src.models.clinica import Clinica
from src.models.pacientes import Pacientes_de_Clinica as Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.NotFound import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    PacienteDuplicadoException,
    MedicoDuplicadoException,
    DatosInvalidosException
)


class TestClinica(unittest.TestCase):
    
    def setUp(self):
        self.clinica = Clinica()
        # Pacientes según test_pacientes.py
        self.paciente1 = Paciente("Gonzalo Rodríguez", "27654321", "14/08/2001")
        self.paciente2 = Paciente("Maria Barbosa", "74518234", "19/11/1970")
        # Médicos según test_medico.py
        self.medico1 = Medico("Dra. Maria Etchegoyen", "48900126")
        self.medico1.agregar_especialidad(Especialidad("Pediatría", ["lunes", "miércoles", "jueves"]))
        self.medico2 = Medico("Dra. María García", "5678")
        self.medico2.agregar_especialidad(Especialidad("Podologia", ["martes", "viernes"]))

    def test_registro_exitoso_paciente(self):
        self.clinica.agregar_paciente(self.paciente1)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "27654321")

    def test_registro_exitoso_medico(self):
        self.clinica.agregar_medico(self.medico1)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "48900126")

    def test_prevencion_paciente_duplicado(self):
        self.clinica.agregar_paciente(self.paciente1)
        paciente_duplicado = Paciente("Juan Martínez", "27654321", "15/03/1992")
        with self.assertRaises(PacienteDuplicadoException):
            self.clinica.agregar_paciente(paciente_duplicado)

    def test_prevencion_medico_duplicado(self):
        self.clinica.agregar_medico(self.medico1)
        medico_duplicado = Medico("Dr. mariano blajebitch", "48900126")
        with self.assertRaises(MedicoDuplicadoException):
            self.clinica.agregar_medico(medico_duplicado)

    def test_datos_invalidos_paciente(self):
        with self.assertRaises(DatosInvalidosException):
            self.clinica.agregar_paciente("no es un paciente")

    def test_datos_invalidos_medico(self):
        with self.assertRaises(DatosInvalidosException):
            self.clinica.agregar_medico("no es un médico")

    def test_agregar_especialidad_medico_registrado(self):
        self.clinica.agregar_medico(self.medico1)
        medico = self.clinica.obtener_medico_por_matricula("48900126")
        nueva_especialidad = Especialidad("Neurología", ["sábado"])
        medico.agregar_especialidad(nueva_especialidad)
        especialidades = medico.obtener_especialidades()
        self.assertEqual(len(especialidades), 2)

    def test_error_medico_no_registrado(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.obtener_medico_por_matricula("9999")

    def test_agendar_turno_exitoso(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)  # lunes
        self.clinica.agendar_turno("27654321", "48900126", "Pediatría", fecha_turno)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_evitar_turnos_duplicados(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_paciente(self.paciente2)
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)  # lunes
        self.clinica.agendar_turno("27654321", "48900126", "Pediatría", fecha_turno)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("74518234", "48900126", "Pediatría", fecha_turno)

    def test_error_paciente_no_existe_turno(self):
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("34857364", "48900126", "Pediatría", fecha_turno)

    def test_error_medico_no_existe_turno(self):
        self.clinica.agregar_paciente(self.paciente1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("27654321", "283462", "Pediatría", fecha_turno)

    def test_error_especialidad_no_disponible(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("27654321", "48900126", "Cardiología", fecha_turno)

    def test_error_medico_no_trabaja_ese_dia(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 17, 10, 0)  # martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("27654321", "48900126", "Pediatría", fecha_turno)

    def test_emitir_receta_exitosa(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        self.clinica.emitir_receta("27654321", "48900126", ["Paracetamol", "Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("27654321")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)

    def test_error_paciente_no_existe_receta(self):
        self.clinica.agregar_medico(self.medico1)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "48900126", ["Paracetamol"])

    def test_error_medico_no_existe_receta(self):
        self.clinica.agregar_paciente(self.paciente1)
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("27654321", "9999", ["Paracetamol"])

    def test_error_medicamentos_vacios(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("27654321", "48900126", [])

    def test_obtener_historia_clinica_completa(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        fecha_turno = datetime(2025, 6, 16, 10, 0)
        self.clinica.agendar_turno("27654321", "48900126", "Pediatría", fecha_turno)
        self.clinica.emitir_receta("27654321", "48900126", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("27654321")
        turnos = historia.obtener_turnos()
        recetas = historia.obtener_recetas()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(len(recetas), 1)

    def test_error_historia_paciente_no_registrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica("99999999")

    def _obtener_proximo_lunes(self):
        hoy = datetime.now()
        dias_hasta_lunes = (0 - hoy.weekday()) % 7 
        if dias_hasta_lunes == 0:  
            dias_hasta_lunes = 7
        return hoy + timedelta(days=dias_hasta_lunes)

    def _obtener_proximo_martes(self):
        hoy = datetime.now()
        dias_hasta_martes = (1 - hoy.weekday()) % 7  
        if dias_hasta_martes == 0: 
            dias_hasta_martes = 7
        return hoy + timedelta(days=dias_hasta_martes)

    def _obtener_fecha_fija_lunes(self):
        return datetime(2025, 6, 16, 10, 0)

    def _obtener_fecha_fija_martes(self):
        return datetime(2025, 6, 17, 10, 0)

if __name__ == "__main__":
    unittest.main()