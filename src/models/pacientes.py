import re
from datetime import datetime

class pacientes_de_clinca:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self._validar_nombre(nombre)
        self._validar_dni(dni)
        self._validar_fecha_nacimiento(fecha_nacimiento)
        
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento

   
    def obtener_dni(self) -> str:
        return self.__dni

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"
