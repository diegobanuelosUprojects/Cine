class Administracion:
    def administracionAsientos(self):
        print("Administracion de asientos: ")
        print(self.SeatsAvailable)
        print(self.SeatsReserved)
        seat = input("Seleccione un asiento: ")
        try:
            if self.SeatsAvailable[seat] == True:
                print("Asiento disponible: ", seat)
                self.SeatsAvailable[seat] = False
                print("Asiento reservado correctamente: ", seat)
                self.SeatsReserved[seat] = {seat}
        except KeyError:
            print("Asiento no disponible, seleccione otro: ", seat)
    def cancelarReservacion(self):
        print("Cancelar reservacion: ")
        print(self.SeatsReserved)
        seat = input("Seleccione un asiento: ")
        try:
         if self.SeatsReserved[seat] == True:
            print("Asiento reservado: ", seat)
            self.SeatsReserved[seat] = False
            print("Asiento cancelado correctamente: ", seat)
        except KeyError:
            print("Asiento no reservado, seleccione otro: ", seat)
