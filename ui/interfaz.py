from reservas.reservas import Reservas
from admin.administracion import Administracion
from reportes.reportes import Reportes
from auth.autenticacion import Autenticacion
import os

class Cine(Reservas, Administracion, Reportes, Autenticacion):
    session = False
    def __init__(self):
        self.SeatsAvailable = {"A1":True, "A2":True, "A3":True, "A4":True, "A5":True, "A6":True, "A7":True, "A8":True, "A9":True, "A10":True}
        self.SeatsReserved = {}

def iniciar_interfaz():
    cine = Cine()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. reservar asientos")
        print("2. Mi reservacion")
        if cine.session == False:
            print("3. Iniciar Sesion")
        if cine.session == True:
            print("3. Administracion")
            print("4. Salir")
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
            if option == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("1. Registrar Asiento.")
                print("2. Cancelar Asiento.")
                print("3. Porcentajes de Asientos Disponibles.")
                print("4. porcentaje de Asientos Reservados.")
                print("5. volver.")
                option = input("Seleccione una opción: ")
                if option == "1":
                    cine.administracionAsientos()
                elif option == "2":
                    cine.cancelarReservacion()
                elif option == "3":
                    cine.PorcentajeDisponibles()
                elif option == "4":
                    cine.PorcentajeReservados()
        elif option == "4":
            break
