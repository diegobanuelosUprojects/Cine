class Autenticacion:
    def iniciarSesion(self):
        self.session = False
        print("Inicia sesion: ")
        Username = input("Ingrese su nombre de usuario: ")
        Password = input("Ingrese su contraseña: ")
        if Username == "admin" and Password == "123456":
            print("Inicio de sesion exitoso")
            self.session = True
        else:
            print("Inicio de sesion fallido")
