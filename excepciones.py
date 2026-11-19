"""Excepciones personalizadas del sistema Software FJ."""

class SoftwareFJError(Exception):
    """Excepción base para los errores controlados del sistema."""

class DatosInvalidosError(SoftwareFJError):
    """Se genera cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(SoftwareFJError):
    """Se genera cuando un servicio no está disponible."""

class ReservaNoPermitidaError(SoftwareFJError):
    """Se genera cuando una operación sobre una reserva no está permitida."""
