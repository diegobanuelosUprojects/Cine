import os

class Administracion:
    def cancelarReservacion(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print(" " * 14 + "CANCELAR RESERVACIÓN")
        print("=" * 50)
        reservas_activas = [s for s, act in self.SeatsReserved.items() if act is True]
        if not reservas_activas:
            print("\033[31mNo hay reservaciones activas para cancelar.\033[0m")
            print("=" * 50)
            input("\nPresiona enter para continuar...")
            return

        print("Reservaciones activas:")
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
        print(f"Total actual acumulado: ${total:.2f}")
        print("=" * 50)
        print("(Escriba 'salir' para cancelar la operación)")
        seat_input = input("\nSeleccione el asiento que desea cancelar: ").strip()
        if seat_input.lower() == "salir":
            return

        seat = seat_input.upper()
        if seat in self.SeatsReserved and self.SeatsReserved[seat] is True:
            self.SeatsReserved[seat] = False
            self.SeatsAvailable[seat] = True
            nuevo_total = self.calcularTotalReservacion()
            print(f"\n\033[32mAsiento {seat} cancelado correctamente.\033[0m")
            print(f"Nuevo total de reservación: \033[32m${nuevo_total:.2f}\033[0m")
        else:
            print(f"\n\033[31mEl asiento '{seat_input}' no está reservado o no es válido.\033[0m")
        input("\nPresiona enter para continuar...")

    def administracionTarifasYAsientos(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 60)
            print(" " * 12 + "ADMINISTRACIÓN DE TARIFAS Y ASIENTOS (PB-7)")
            print("=" * 60)
            print("Tarifas configuradas para el negocio:")
            print(f"  • \033[33mPreferente\033[0m: ${self.Tarifas.get('Preferente', 0.0):.2f}")
            print(f"  • \033[36mEstándar\033[0m:   ${self.Tarifas.get('Estándar', 0.0):.2f}")
            print("-" * 60)
            print(f"{"Asiento":<10} {"Tipo":<15} {"Tarifa":<12} {"Estado":<12}")
            print("-" * 60)
            for seat, available in self.SeatsAvailable.items():
                tipo = self.obtenerTipoAsiento(seat)
                precio = self.obtenerPrecioAsiento(seat)
                tipo_fmt = f"\033[33m{tipo:<15}\033[0m" if tipo == "Preferente" else f"\033[36m{tipo:<15}\033[0m"
                status_fmt = "\033[32mDisponible\033[0m" if available else "\033[31mReservado\033[0m"
                print(f"{seat:<10} {tipo_fmt} ${precio:<10.2f} {status_fmt}")
            print("=" * 60)
            print("1. Modificar tarifas de precios")
            print("2. Cambiar tipo de asiento (Preferente <-> Estándar)")
            print("3. Volver al menú principal")
            opc = input("\nSeleccione una opción: ").strip()
            if opc == "1":
                self.modificarTarifas()
            elif opc == "2":
                self.cambiarTipoAsiento()
            elif opc in ("3", "salir", "Salir"):
                break

    def modificarTarifas(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print(" " * 14 + "MODIFICAR TARIFAS (PB-7)")
        print("=" * 50)
        print(f"Tarifa Preferente actual: ${self.Tarifas.get('Preferente', 0.0):.2f}")
        print(f"Tarifa Estándar actual:   ${self.Tarifas.get('Estándar', 0.0):.2f}")
        print("-" * 50)

        pref_input = input("Nueva tarifa para Preferente (Enter para mantener): ").strip()
        if pref_input:
            try:
                nuevo_pref = float(pref_input)
                if nuevo_pref >= 0:
                    self.Tarifas["Preferente"] = nuevo_pref
                    print(f"\033[32mTarifa Preferente actualizada a ${nuevo_pref:.2f}\033[0m")
                else:
                    print("\033[31mEl precio no puede ser negativo.\033[0m")
            except ValueError:
                print("\033[31mValor inválido para tarifa Preferente.\033[0m")

        std_input = input("Nueva tarifa para Estándar (Enter para mantener): ").strip()
        if std_input:
            try:
                nuevo_std = float(std_input)
                if nuevo_std >= 0:
                    self.Tarifas["Estándar"] = nuevo_std
                    print(f"\033[32mTarifa Estándar actualizada a ${nuevo_std:.2f}\033[0m")
                else:
                    print("\033[31mEl precio no puede ser negativo.\033[0m")
            except ValueError:
                print("\033[31mValor inválido para tarifa Estándar.\033[0m")

        input("\nPresiona enter para continuar...")

    def cambiarTipoAsiento(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print(" " * 10 + "Cambiar clasificacion de asiento")
        print("=" * 50)
        print(f"{"Asiento":<10} {"Tipo Actual":<15} {"Tarifa Actual":<15}")
        print("-" * 50)
        for seat in self.SeatsAvailable:
            tipo = self.obtenerTipoAsiento(seat)
            precio = self.obtenerPrecioAsiento(seat)
            tipo_fmt = f"\033[33m{tipo:<15}\033[0m" if tipo == "Preferente" else f"\033[36m{tipo:<15}\033[0m"
            print(f"{seat:<10} {tipo_fmt} ${precio:<13.2f}")
        print("-" * 50)

        seat_input = input("Ingrese el asiento que desea cambiar (o 'salir'): ").strip()
        if seat_input.lower() == "salir":
            return

        seat = seat_input.upper()
        if seat not in self.SeatsAvailable:
            print(f"\033[31mEl asiento '{seat_input}' no es válido.\033[0m")
        else:
            tipo_actual = self.obtenerTipoAsiento(seat)
            nuevo_tipo = "Estándar" if tipo_actual == "Preferente" else "Preferente"
            self.SeatTypes[seat] = nuevo_tipo
            nueva_tarifa = self.obtenerPrecioAsiento(seat)
            print(f"\n\033[32mEl asiento {seat} ahora es '{nuevo_tipo}'.\033[0m")
            print(f"Nueva tarifa aplicable: ${nueva_tarifa:.2f}")
        input("\nPresiona enter para continuar...")

    def administracionAsientos(self):
        self.administracionTarifasYAsientos()

