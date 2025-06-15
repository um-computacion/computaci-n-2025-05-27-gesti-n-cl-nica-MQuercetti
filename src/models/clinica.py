from datetime import datetime
from .pacientes import Pacientes_de_Clinica as Paciente
from .medico import Medico
from .turnos import Turno
from .receta import Receta
from .historia_clinica import HistoriaClinica
from .NotFound import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    PacienteDuplicadoException,
    MedicoDuplicadoException,
    DatosInvalidosException
)


class Clinica:
    def __init__(self):
        self.__pacientes = {}  
        self.__medicos = {}    
        self.__turnos = []
        self.__historias_clinicas = {} 

    def agregar_paciente(self, paciente: Paciente):
       
        if not isinstance(paciente, Paciente):
            raise DatosInvalidosException("El parámetro debe ser una instancia de Paciente")
        
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise PacienteDuplicadoException(f"Ya existe un paciente con DNI {dni}")
        
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
    
        if not isinstance(medico, Medico):
            raise DatosInvalidosException("El parámetro debe ser una instancia de Medico")
        
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise MedicoDuplicadoException(f"Ya existe un médico con matrícula {matricula}")
        
        self.__medicos[matricula] = medico

    def obtener_pacientes(self) -> list[Paciente]:
       
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
       
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
       
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
       
        
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
       
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        
       
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        
        
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        
        
        self.__historias_clinicas[dni].agregar_turno(turno)

    def obtener_turnos(self) -> list[Turno]:
        """Devuelve todos los turnos agendados."""
        return self.__turnos.copy()

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
       
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
       
        receta = Receta(paciente, medico, medicamentos)
        
       
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
       
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    def validar_existencia_paciente(self, dni: str):
       
        if not dni or dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No se encontró un paciente con DNI {dni}")

    def validar_existencia_medico(self, matricula: str):
        
        if not matricula or matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No se encontró un médico con matrícula {matricula}")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
       
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(f"El médico ya tiene un turno agendado para {fecha_hora.strftime('%d/%m/%Y %H:%M')}")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
       
        dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return dias_semana[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str:
       
        especialidad = medico.obtener_especialidad_para_dia(dia_semana)
        if not especialidad:
            raise MedicoNoDisponibleException(f"El médico no atiende los {dia_semana}")
        return especialidad

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
       
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        
        if not especialidad_disponible:
            raise MedicoNoDisponibleException(f"El Dr. {medico.obtener_nombre()} no atiende los {dia_semana}")
        
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(
                f"El Dr. {medico.obtener_nombre()} no atiende {especialidad_solicitada} los {dia_semana}. "
                f"Ese día atiende: {especialidad_disponible}"
            )