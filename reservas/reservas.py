import os

class Reservas:
    def obtenerTipoAsiento(self, seat):
        return self.SeatTypes.get(seat, "Estándar")

    def obtenerPrecioAsiento(self, seat):
        tipo = self.obtenerTipoAsiento(seat)
        return self.Tarifas.get(tipo, 0.0)

    def calcularTotalReservacion(self):
        total = 0.0
        for seat, activo in self.SeatsReserved.items():
            if activo is True:
                total += self.obtenerPrecioAsiento(seat)
        return total

    def reservarAsientos(self):
        if not any(self.SeatsAvailable.values()):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n¡Lo sentimos! La sala está llena. No hay asientos disponibles.")
            input("\nPresiona enter para volver al menú...")
            return
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" " * 20 + "RESERVAR ASIENTOS")
            print(f"  • \033[33mPreferente\033[0m: ${self.Tarifas.get('Preferente', 0.0):.2f} (Filas premium / mejor visibilidad)")
            print(f"  • \033[36mEstándar\033[0m:   ${self.Tarifas.get('Estándar', 0.0):.2f}")
            print(f"{"Asiento":<10} {"Tipo":<15} {"Precio":<12} {"Estado":<12}")
            for seat, available in self.SeatsAvailable.items():
                tipo = self.obtenerTipoAsiento(seat)
                precio = self.obtenerPrecioAsiento(seat)
                tipo_fmt = f"\033[33m{tipo:<15}\033[0m" if tipo == "Preferente" else f"\033[36m{tipo:<15}\033[0m"
                status_fmt = "\033[32mDisponible\033[0m" if available else "\033[31mNo disponible\033[0m"
                print(f"{seat:<10} {tipo_fmt} ${precio:<10.2f} {status_fmt}")
            print("-" * 60)

            reservas_activas = [s for s, act in self.SeatsReserved.items() if act is True]
            if reservas_activas:
                total_actual = self.calcularTotalReservacion()
                print(f"Tus reservas: {', '.join(reservas_activas)} | Total acumulado: \033[32m${total_actual:.2f}\033[0m")

            print("(Escriba 'salir' para volver al menú)")
            seat_input = input("\nSeleccione un asiento: ").strip()
            if seat_input.lower() == "salir":
                return

            seat = seat_input.upper()
            if seat not in self.SeatsAvailable:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31mLa opcion no es valida, vuelve a intentarlo.\033[0m")
                input("\nPresiona enter para continuar...")
                continue

            if not self.SeatsAvailable[seat]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31mEl asiento {seat} ya está reservado o no disponible.\033[0m")
                input("\nPresiona enter para continuar...")
                continue

            # Reservar asiento
            self.SeatsAvailable[seat] = False
            self.SeatsReserved[seat] = True

            tipo = self.obtenerTipoAsiento(seat)
            precio = self.obtenerPrecioAsiento(seat)
            total = self.calcularTotalReservacion()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(" " * 13 + "\033[32m¡ASIENTO RESERVADO!\033[0m")
            print(f"Asiento:              {seat}")
            print(f"Tipo de asiento:      {tipo}")
            print(f"Tarifa del asiento:   ${precio:.2f}")
            print("-" * 50)
            print(f"\033[32mPRECIO TOTAL ACUMULADO: ${total:.2f}\033[0m")

            seguir = input("\n¿Desea reservar otro asiento? (s/n): ").strip().lower()
            if seguir not in ("s", "si", "sí"):
                break

    def miReservacion(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        reservas_activas = [s for s, act in self.SeatsReserved.items() if act is True]
        if not reservas_activas:
            print("=" * 50)
            print(" " * 17 + "MI RESERVACIÓN")
            print("=" * 50)
            print("\033[31mNo tienes reservaciones\033[0m")
            print("=" * 50)
        else:
            print("=" * 50)
            print(" " * 17 + "MI RESERVACIÓN")
            print("=" * 50)
            print("Tus reservaciones:")
            print(f"{"Asiento":<10} {"Tipo":<15} {"Precio":<10}")
            print("-" * 50)
            total = 0.0
            for seat in reservas_activas:
                tipo = self.obtenerTipoAsiento(seat)
                precio = self.obtenerPrecioAsiento(seat)
                total += precio
                tipo_fmt = f"\033[33m{tipo:<15}\033[0m" if tipo == "Preferente" else f"\033[36m{tipo:<15}\033[0m"
                print(f"{seat:<10} {tipo_fmt} ${precio:<9.2f}")
            print("-" * 50)
            print(f"Cantidad de asientos: {len(reservas_activas)}")
            print(f"\033[32mPRECIO TOTAL A PAGAR: ${total:.2f}\033[0m")
            print("=" * 50)
        input("\nPresiona enter para continuar...")
