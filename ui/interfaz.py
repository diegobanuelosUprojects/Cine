from reservas.reservas import Reservas
from admin.administracion import Administracion
from reportes.reportes import Reportes
from auth.autenticacion import Autenticacion
import os

class Cine(Reservas, Administracion, Reportes, Autenticacion):
    session = False
    def __init__(self):
        # Asientos del cine
        self.SeatsAvailable = {
            "A1": True, "A2": True, "A3": True, "A4": True, "A5": True,
            "A6": True, "A7": True, "A8": True, "A9": True, "A10": True
        }
        # PB-7: Distinción de asientos preferentes vs estándar
        self.SeatTypes = {
            "A1": "Preferente",
            "A2": "Preferente",
            "A3": "Preferente",
            "A4": "Preferente",
            "A5": "Preferente",
            "A6": "Estándar",
            "A7": "Estándar",
            "A8": "Estándar",
            "A9": "Estándar",
            "A10": "Estándar"
        }
        # PB-7: Tarifas diferenciadas por tipo de asiento
        self.Tarifas = {
            "Preferente": 100.0,
            "Estándar": 60.0
        }
        self.SeatsReserved = {}

def iniciar_interfaz():
    cine = Cine()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" " * 14 + "ASIENTOS DISPONIBLES")
        print(f"{'Asiento':<10} {'Tipo':<15} {'Estado':<12}")
        for seat, available in cine.SeatsAvailable.items():
            tipo = cine.obtenerTipoAsiento(seat)
            estado = "Disponible" if available else "No disponible"
            print(f"{seat:<10} {tipo:<15} {estado:<12}")
        print("-" * 55)
        print("1. Reservar asientos")
        print("2. Mi reservación")
        if cine.session is False:
            print("3. Iniciar Sesión (Admin)")
            print("4. Salir")
        else:
            print("3. Cancelar reservación")
            print("4. Porcentaje de asientos disponibles")
            print("5. Porcentaje de asientos reservados")
            print("6. Administrar tarifas y asientos preferentes (PB-7)")
            print("7. Cerrar Sesión")
            print("8. Salir")
        print("-" * 45)
        option = input("Seleccione una opción: ").strip()

        if option == "1":
            cine.reservarAsientos()
        elif option == "2":
            cine.miReservacion()
        elif cine.session is False:
            if option == "3":
                cine.iniciarSesion()
            elif option in ("4", "salir", "Salir"):
                break
        else:
            if option == "3":
                try:
                    cine.cancelarReservacion()
                except Exception as e:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\033[31mHubo un error y no se pudo cancelar la reservación: {e}\033[0m")
                    input("\nPresiona enter para continuar...")
            elif option == "4":
                cine.PorcentajeDisponibles()
            elif option == "5":
                cine.PorcentajeReservados()
            elif option == "6":
                cine.administracionTarifasYAsientos()
            elif option == "7":
                cine.cerrarSesion()
            elif option in ("8", "salir", "Salir"):
                break

