"""Gestión de reservas y registro de operaciones."""
from datetime import datetime
from excepciones import ReservaNoPermitidaError, ServicioNoDisponibleError


class Reserva:
    """Relaciona un cliente con un servicio, duración, costo y estado."""

    ESTADOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA")

    def __init__(self, codigo, cliente, servicio, horas):
        if cliente is None or servicio is None:
            raise ReservaNoPermitidaError("La reserva requiere cliente y servicio.")
        servicio.validar_disponibilidad()
        servicio.validar_parametros(horas)
        self.codigo = str(codigo)
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "PENDIENTE"
        self.fecha_creacion = datetime.now()
        self.costo = servicio.calcular_costo(horas)

    def confirmar(self):
        if self.estado != "PENDIENTE":
            raise ReservaNoPermitidaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = "CONFIRMADA"
        return f"Reserva {self.codigo} confirmada."

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise ReservaNoPermitidaError("La reserva ya está cancelada.")
        self.estado = "CANCELADA"
        return f"Reserva {self.codigo} cancelada."

    def procesar(self):
        if self.estado != "CONFIRMADA":
            raise ReservaNoPermitidaError("La reserva debe estar confirmada para procesarse.")
        return f"Reserva {self.codigo} procesada por ${self.costo:,.2f}."

    def __str__(self):
        return (f"{self.codigo} | {self.cliente.nombre} | {self.servicio.nombre} | "
                f"{self.horas} hora(s) | ${self.costo:,.2f} | {self.estado}")
