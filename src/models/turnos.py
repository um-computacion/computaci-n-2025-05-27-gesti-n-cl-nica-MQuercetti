from datetime import datetime
from .NotFound import DatosInvalidosException


class Turno:
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        self._validar_parametros(paciente, medico, fecha_hora, especialidad)
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad.strip()

    def _validar_parametros(self, paciente, medico, fecha_hora, especialidad):
        if paciente is None:
            raise DatosInvalidosException("El paciente no puede ser None")
        
        if medico is None:
            raise DatosInvalidosException("El médico no puede ser None")
        
        if not isinstance(fecha_hora, datetime):
            raise DatosInvalidosException("La fecha_hora debe ser un objeto datetime")
        
        if fecha_hora < datetime.now():
            raise DatosInvalidosException("No se pueden agendar turnos en el pasado")
        
        if not especialidad or not especialidad.strip():
            raise DatosInvalidosException("La especialidad no puede estar vacía")

    def obtener_paciente(self):
        return self.__paciente

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def obtener_especialidad(self) -> str:
        return self.__especialidad

    def __str__(self) -> str:
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        nombre_medico = self.__medico.obtener_nombre()
        for prefijo in ("Dr. ", "Dra. "):
            if nombre_medico.startswith(prefijo):
                nombre_medico = nombre_medico[len(prefijo):]
        nombre_medico = "Dr. " + nombre_medico
        return f"Turno: {self.__paciente.obtener_nombre()}, {nombre_medico}, {self.__especialidad}, {fecha_str}"

    def __repr__(self) -> str:
        return (f"Turno({self.__paciente.obtener_nombre()}, "
                f"{self.__medico.obtener_nombre()}, "
                f"{self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}, "
                f"{self.__especialidad})")

    def __eq__(self, other):
        if not isinstance(other, Turno):
            return False
        return (self.__paciente == other.__paciente and
                self.__medico == other.__medico and
                self.__fecha_hora == other.__fecha_hora and
                self.__especialidad == other.__especialidad)