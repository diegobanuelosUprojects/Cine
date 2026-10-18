import os


class Reportes:
    def PorcentajeDisponibles(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        total_asientos = len(self.SeatsAvailable) + len(self.SeatsReserved)
        asientos_disponibles = len([seat for seat in self.SeatsAvailable if self.SeatsAvailable[seat] == True])
        porcentaje_disponibles = (asientos_disponibles / total_asientos) * 100
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Porcentaje de asientos disponibles: ", porcentaje_disponibles, "%")
        input("Presiona enter para continuar...")
    def PorcentajeReservados(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        total_asientos = len(self.SeatsAvailable) + len(self.SeatsReserved)
        asientos_reservados = len([seat for seat in self.SeatsReserved if self.SeatsReserved[seat] == True])
        porcentaje_reservados = (asientos_reservados / total_asientos) * 100
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Porcentaje de asientos reservados: ", porcentaje_reservados, "%")
        input("Presiona enter para continuar...")

