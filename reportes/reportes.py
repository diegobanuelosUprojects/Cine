import os

class Reportes:
    def PorcentajeDisponibles(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        total_asientos = len(self.SeatsAvailable)
        asientos_disponibles = len([seat for seat, available in self.SeatsAvailable.items() if available is True])
        porcentaje_disponibles = (asientos_disponibles / total_asientos) * 100 if total_asientos > 0 else 0
        print(" " * 12 + "REPORTE DE DISPONIBILIDAD")
        print(f"Total de asientos:        {total_asientos}")
        print(f"Asientos disponibles:     {asientos_disponibles}")
        print(f"Porcentaje disponibles:   \033[32m{round(porcentaje_disponibles, 2)}%\033[0m")
        print("=" * 50)
        input("\nPresiona enter para continuar...")

    def PorcentajeReservados(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        total_asientos = len(self.SeatsAvailable)
        asientos_reservados = len([seat for seat, reservado in self.SeatsReserved.items() if reservado is True])
        porcentaje_reservados = (asientos_reservados / total_asientos) * 100 if total_asientos > 0 else 0
        total_ingresos = self.calcularTotalReservacion() if hasattr(self, 'calcularTotalReservacion') else 0.0
        print("=" * 50)
        print(" " * 13 + "REPORTE DE OCUPACIÓN")
        print("=" * 50)
        print(f"Total de asientos:        {total_asientos}")
        print(f"Asientos reservados:      {asientos_reservados}")
        print(f"Porcentaje reservados:    \033[33m{round(porcentaje_reservados, 2)}%\033[0m")
        print(f"Ingresos por reservas:    \033[32m${total_ingresos:.2f}\033[0m")
        print("=" * 50)
        input("\nPresiona enter para continuar...")

