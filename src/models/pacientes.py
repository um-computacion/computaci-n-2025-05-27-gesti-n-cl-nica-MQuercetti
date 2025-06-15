import re
from datetime import datetime
from .NotFound import DatosInvalidosException

class Pacientes_de_Clinica:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self._validar_nombre(nombre)
        self._validar_dni(dni)
        self._validar_fecha_nacimiento(fecha_nacimiento)
        
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento

    def _validar_nombre(self, nombre: str):
        
        if not nombre or not nombre.strip():
            raise DatosInvalidosException("El nombre esta vacío, llenalo")

        if any(char.isdigit() for char in nombre):
            raise DatosInvalidosException("El nombre no permite números")
        
        nombre_solo_letras = nombre.replace(' ', '').replace('.', '')
        if not nombre_solo_letras.isalpha():
            raise DatosInvalidosException("El nombre solo pone tu nombre y apellido, sin caracteres especiales")

    def _validar_dni(self, dni: str):
        
        if not dni or not dni.strip():
            raise DatosInvalidosException("El DNI no puede estar vacío sino no naciste todavia")
        
        dni_limpio = dni.strip()
        if not (dni_limpio.isdigit() and 7 <= len(dni_limpio) <= 8):
            raise DatosInvalidosException("El DNI debe teniene 8 digitos pone esos nada mas")

    def _validar_fecha_nacimiento(self, fecha: str):
       
        if not fecha or not fecha.strip():
            raise DatosInvalidosException("La fecha de nacimiento no puede estar vacía ")
        
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise DatosInvalidosException("La fecha debe estar en dd/mm/aaaa y ser una que exista")

    def obtener_dni(self) -> str:
        return self.__dni

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"
