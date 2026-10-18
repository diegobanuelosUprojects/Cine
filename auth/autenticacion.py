import os
class Autenticacion:
    def iniciarSesion(self):
        self.session = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Inicia sesion: ")
        Username = input("Ingrese su nombre de usuario: ")
        Password = input("Ingrese su contraseña: ")
        if Username == "admin" and Password == "123456":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inicio de sesion exitoso")
            self.session = True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inicio de sesion fallido")
            input("Presiona enter para continuar...")
