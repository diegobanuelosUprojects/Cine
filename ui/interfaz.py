from reservas.reservas import Reservas
from admin.administracion import Administracion
from reportes.reportes import Reportes
from auth.autenticacion import Autenticacion

class Cine(Reservas, Administracion, Reportes, Autenticacion):
    session = False
    def __init__(self):
        self.SeatsAvailable = {"A1":True, "A2":True, "A3":True, "A4":True, "A5":True, "A6":True, "A7":True, "A8":True, "A9":True, "A10":True}
        self.SeatsReserved = {}

def iniciar_interfaz():
    cine = Cine()
    while True:
        print("1. reservar asientos")
        print("2. Mi reservacion")
        if cine.session == False:
            print("3. Iniciar Sesion")
        if cine.session == True:
            print("3. Administracion de asientos")
            print("4. Ver porcentaje de asientos")
            print("5. Cancelar Reservacion de asientos")
            print("6. Salir")
        else:
            print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
                cine.reservarAsientos()
        elif option == "2":
                cine.miReservacion()
        if cine.session == False:
           if option == "3":
             cine.iniciarSesion()

        if cine.session == True:
            if option == "4":
                cine.administracionAsientos()
        elif option == "5":
            cine.verPorcentajeAsientos()
        elif option == "6":
            cine.cancelarReservacion()
        elif option == "7":
            break
        else:
            if option == "4":
                break;
