"""Gestor en memoria para clientes, servicios y reservas."""
import logging
from excepciones import DatosInvalidosError, SoftwareFJError

logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)


class GestorSoftwareFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if any(c.identificador == cliente.identificador for c in self.clientes):
            raise DatosInvalidosError("Ya existe un cliente con ese identificador.")
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.identificador)
        return cliente

    def registrar_servicio(self, servicio):
        if any(s.codigo == servicio.codigo for s in self.servicios):
            raise DatosInvalidosError("Ya existe un servicio con ese código.")
        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.codigo)
        return servicio

    def crear_reserva(self, codigo, cliente, servicio, horas):
        reserva = __import__("reservas").Reserva(codigo, cliente, servicio, horas)
        self.reservas.append(reserva)
        logging.info("Reserva creada: %s", codigo)
        return reserva

    def buscar_cliente(self, identificador):
        return next((c for c in self.clientes if c.identificador == identificador), None)

    def buscar_servicio(self, codigo):
        return next((s for s in self.servicios if s.codigo == codigo), None)

    def listar_reservas(self):
        return list(self.reservas)
