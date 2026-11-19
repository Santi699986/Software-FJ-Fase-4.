"""Punto de entrada. Ejecuta una demostración de 12 operaciones."""
import logging
from entidades import Cliente, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from gestor import GestorSoftwareFJ
from excepciones import SoftwareFJError, DatosInvalidosError

def ejecutar_demo():
    gestor = GestorSoftwareFJ()
    print("=== SISTEMA INTEGRAL SOFTWARE FJ ===")
    operaciones = 0

    # 1. Registro válido de cliente.
    cliente1 = Cliente("C001", "Laura Pérez", "laura@email.com", "3001234567")
    gestor.registrar_cliente(cliente1); operaciones += 1
    print("1. Cliente registrado:", cliente1.describir())

    # 2. Segundo cliente válido.
    cliente2 = Cliente("C002", "Carlos Gómez", "carlos@email.com", "3017654321")
    gestor.registrar_cliente(cliente2); operaciones += 1
    print("2. Cliente registrado:", cliente2.describir())

    # 3. Registro inválido: correo sin formato correcto.
    try:
        Cliente("C003", "Ana Ruiz", "correo-invalido", "3001234568")
    except DatosInvalidosError as error:
        logging.exception("Operación 3: registro de cliente inválido")
        print("3. Error controlado:", error)
    operaciones += 1

    # 4, 5 y 6. Registro de tres tipos de servicios.
    sala = ReservaSalas("S001", "Sala de reuniones", 50000, 12)
    equipos = AlquilerEquipos("E001", "Computador portátil", 15000, 5)
    asesoria = AsesoriaEspecializada("A001", "Asesoría de software", 80000, "Desarrollo")
    for numero, servicio in enumerate((sala, equipos, asesoria), start=4):
        gestor.registrar_servicio(servicio)
        print(f"{numero}. Servicio registrado:", servicio.describir())
        operaciones += 1

    # 7. Intento de crear un servicio con tarifa inválida.
    try:
        ReservaSalas("S002", "Sala inválida", -1000, 10)
    except DatosInvalidosError as error:
        logging.exception("Operación 7: servicio inválido")
        print("7. Error controlado:", error)
    operaciones += 1

    # 8. Reserva de sala exitosa.
    reserva1 = gestor.crear_reserva("R001", cliente1, sala, 2)
    print("8. Reserva creada:", reserva1)
    operaciones += 1

    # 9. Confirmar y procesar reserva.
    print("9.", reserva1.confirmar())
    operaciones += 1

    # 10. Procesar reserva confirmada.
    print("10.", reserva1.procesar())
    operaciones += 1

    # 11. Intento de reserva con servicio no disponible.
    equipos.disponible = False
    try:
        gestor.crear_reserva("R002", cliente2, equipos, 3)
    except SoftwareFJError as error:
        logging.exception("Operación 11: servicio no disponible")
        print("11. Error controlado:", error)
    operaciones += 1

    # 12. Cancelar una reserva.
    reserva2 = gestor.crear_reserva("R003", cliente2, asesoria, 1)
    print("12.", reserva2.cancelar())
    operaciones += 1

    print(f"\nTotal de operaciones simuladas: {operaciones}")
    print("Reservas registradas:")
    for reserva in gestor.listar_reservas():
        print(" -", reserva)
    print("\nLos eventos y errores se guardan en logs/software_fj.log")

if __name__ == "__main__":
    try:
        ejecutar_demo()
    except Exception as error:
        # Encadenamiento: conserva la causa original y la eleva como error de aplicación.
        logging.exception("Error inesperado en la aplicación")
        raise RuntimeError("La aplicación encontró un error no previsto.") from error
    else:
        print("\nEjecución finalizada correctamente.")
    finally:
        print("Fin del proceso de demostración.")
