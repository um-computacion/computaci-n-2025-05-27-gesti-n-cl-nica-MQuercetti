from .NotFound import DatosInvalidosException
class Especialidad:
    DIAS_VALIDOS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    def __init__(self, tipo: str, dias: list[str]):
        self._validar_tipo(tipo)
        self._validar_dias(dias)
        
        self.__tipo = tipo.strip()
        self.__dias = [d.lower().strip() for d in dias]

    def _validar_tipo(self, tipo: str):
        if not tipo or not tipo.strip():
            raise DatosInvalidosException("Ponga un nombre de especialidad válido")

    def _validar_dias(self, dias: list[str]):
        if not dias or len(dias) == 0:
            raise DatosInvalidosException("Debe especificar al menos un día de trabajo")
        
        dias_normalizados = []
        for dia in dias:
            if not dia or not dia.strip():
                raise DatosInvalidosException("Seleccione un dia existente")
            
            dia_normalizado = dia.lower().strip()
            if dia_normalizado not in self.DIAS_VALIDOS:
                raise DatosInvalidosException(f"'{dia}' No es un día que se trabaja. Días que se trabajan: {', '.join(self.DIAS_VALIDOS)}")
            
            if dia_normalizado in dias_normalizados:
                raise DatosInvalidosException(f"El día '{dia}' está puesto más de una vez")
            
            dias_normalizados.append(dia_normalizado)

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        if not dia:
            return False
        return dia.lower().strip() in self.__dias

    def obtener_dias(self) -> list[str]:
        return self.__dias.copy()

    def __str__(self) -> str:
        dias_str = ', '.join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"