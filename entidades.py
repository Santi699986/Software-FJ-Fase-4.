"""Clases del dominio: entidades, clientes y servicios."""
from abc import ABC, abstractmethod
from datetime import datetime
from excepciones import DatosInvalidosError


class Entidad(ABC):
    """Clase abstracta que representa una entidad identificable del sistema."""

    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise DatosInvalidosError("El identificador es obligatorio.")
        self._identificador = identificador.strip()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la entidad."""


class Cliente(Entidad):
    """Cliente con datos personales encapsulados y validados."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise DatosInvalidosError("El correo electrónico no es válido.")
        self._correo = valor.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        texto = str(valor).strip()
        if not texto.isdigit() or len(texto) < 7:
            raise DatosInvalidosError("El teléfono debe contener al menos 7 dígitos.")
        self._telefono = texto

    def describir(self):
        return f"Cliente {self.nombre} | correo: {self.correo} | teléfono: {self.telefono}"


class Servicio(ABC):
    """Clase abstracta base para los servicios ofrecidos por Software FJ."""

    def __init__(self, codigo, nombre, tarifa_hora, disponible=True):
        if not codigo or not str(codigo).strip():
            raise DatosInvalidosError("El código del servicio es obligatorio.")
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise DatosInvalidosError("La tarifa por hora debe ser mayor que cero.")
        self.codigo = str(codigo).strip()
        self.nombre = nombre
        self.tarifa_hora = float(tarifa_hora)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            from excepciones import ServicioNoDisponibleError
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")

    @abstractmethod
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        """Calcula el costo del servicio con parámetros opcionales."""

    @abstractmethod
    def describir(self):
        """Describe el servicio."""

    @abstractmethod
    def validar_parametros(self, horas):
        """Valida los parámetros específicos del servicio."""


class ReservaSalas(Servicio):
    def __init__(self, codigo, nombre, tarifa_hora, capacidad, disponible=True):
        super().__init__(codigo, nombre, tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser un entero positivo.")
        self.capacidad = capacidad

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0 or horas > 24:
            raise DatosInvalidosError("La reserva de sala debe durar entre 0 y 24 horas.")

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        self.validar_parametros(horas)
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.tarifa_hora * horas
        return round(subtotal * (1 + impuesto) * (1 - descuento), 2)

    def describir(self):
        return f"Sala: {self.nombre} | capacidad: {self.capacidad} personas"


class AlquilerEquipos(Servicio):
    def __init__(self, codigo, nombre, tarifa_hora, unidades, disponible=True):
        super().__init__(codigo, nombre, tarifa_hora, disponible)
        if not isinstance(unidades, int) or unidades <= 0:
            raise DatosInvalidosError("Las unidades deben ser un entero positivo.")
        self.unidades = unidades

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0 or horas > 168:
            raise DatosInvalidosError("El alquiler debe durar entre 0 y 168 horas.")

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        self.validar_parametros(horas)
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.tarifa_hora * horas * self.unidades
        return round(subtotal * (1 + impuesto) * (1 - descuento), 2)

    def describir(self):
        return f"Equipo: {self.nombre} | unidades disponibles: {self.unidades}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, codigo, nombre, tarifa_hora, especialidad, disponible=True):
        super().__init__(codigo, nombre, tarifa_hora, disponible)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")
        self.especialidad = especialidad.strip()

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0 or horas > 8:
            raise DatosInvalidosError("La asesoría debe durar entre 0 y 8 horas.")

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        self.validar_parametros(horas)
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.tarifa_hora * horas
        return round(subtotal * (1 + impuesto) * (1 - descuento), 2)

    def describir(self):
        return f"Asesoría: {self.nombre} | especialidad: {self.especialidad}"
