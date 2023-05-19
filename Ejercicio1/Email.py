class Email:
    idCuenta: ""
    dominio: ""
    tipoDeDominio: ""
    contraseña: ""
           
    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDeDominio}"
        
    def getDominio(self):
        return self.dominio
    
    def crearCuenta(self,correo):
        partes = correo.split("@")
        if len(partes) == 2:
            self.idCuenta = partes[0]
            if "." in partes[1]:
                self.dominio,self.tipoDeDominio = partes[1].split(".")
                print("Direccion de correo electronico correcta.")
                self.contraseña = input("Ingrese contraseña:")
                print("Cuenta creada correctamente.\n--------------")
                return True
            else:
                print("La direccion de correo electronico es incorrecta!\n--------------")
        else:
            print("La direccion de correo electronico es incorrecta!\n--------------")
           
    def cambiarContra(self):
        actual= str(input("Ingrese contraseña actual: "))
        while self.contraseña != actual:
            print("Las contraseñas no coinciden!")
            actual = input("Ingrese nuevamente la contraseña: ")
            print("---------------------")
        print("Las contraseñas coinciden :)\n---------------------")
        self.contraseña = input("Ingrese su nueva contraseña: ")
        print("Contraseña cambiada con exito!")
        
    def verificarEmail():
        return