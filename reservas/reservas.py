class Reservas:
    def reservarAsientos(self):
        print("Reservar asientos: ")
        print(self.SeatsAvailable)
        seat = input("Seleccione un asiento: ")
        try:
            if self.SeatsAvailable[seat] == True:
                print("Asiento disponible: ", seat)
                self.SeatsAvailable[seat] = False
                print("Asiento reservado correctamente: ", seat)
                self.SeatsReserved[seat] = {seat}
        except KeyError:
            print("La opcion no es valida, ingresa una valida:")
    def miReservacion(self):
        print("Mi reservacion: ")
        print(self.SeatsReserved)
