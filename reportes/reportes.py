class Reportes:
    def verPorcentajeAsientos(self):
        print("Porcentaje de asientos disponibles: ", (len(self.SeatsAvailable) / len(self.SeatsReserved)) * 100)
        print("Porcentaje de asientos reservados: ", (len(self.SeatsReserved) / len(self.SeatsAvailable)) * 100)
