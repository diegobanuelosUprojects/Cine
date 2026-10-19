import os

class Autenticacion:
    def iniciarSesion(self):
        self.session = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 45)
        print(" " * 14 + "INICIAR SESIÓN")
        print("=" * 45)
        Username = input("Ingrese su nombre de usuario: ").strip()
        Password = input("Ingrese su contraseña: ").strip()
        if Username == "admin" and Password == "123456":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32mInicio de sesion exitoso\033[0m")
            self.session = True
            input("\nPresiona enter para continuar...")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[31mInicio de sesion fallido\033[0m")
            input("\nPresiona enter para continuar...")

    def cerrarSesion(self):
        self.session = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[32mSesión cerrada correctamente.\033[0m")
        input("\nPresiona enter para continuar...")
