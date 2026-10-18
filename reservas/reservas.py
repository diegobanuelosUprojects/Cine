import os
import time

class Reservas:
    def reservarAsientos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Reservar asientos: ")
        print(f"{"Asiento":<10} {"Estado":<10}")
        print("-"*20)
        for seat, available in self.SeatsAvailable.items():
            status = "Disponible" if available else "No disponible"
            print(f"{seat:<10} {status:<10}")
        seat = input("Seleccione un asiento: ")
        if seat.lower() == "salir":
            return
        else:
            try:
                if self.SeatsAvailable[seat] == True:
                    self.SeatsAvailable[seat] = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Asiento reservado correctamente")
                    self.SeatsReserved[seat] = {seat}
                    input("Presiona enter para continuar...")
            except KeyError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("La opcion no es valida, vuelve a intentarlo.")
                input("Presiona enter para continuar...")
    def miReservacion(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(self.SeatsReserved) == 0:
            print("No tienes reservaciones")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tus reservaciones: ")
            for seat in self.SeatsReserved:
                print(seat)
        input("Presiona enter para continuar...")
