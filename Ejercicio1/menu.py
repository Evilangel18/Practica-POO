from Email import Email
import csv
import os
import sys
class Menu:
    op = int
    
    def __init__ (self):
        self.op=None
    
    def manejoMenu (self,op,cuenta):
         if op == 1:
             self.opcion1(cuenta)
         elif op == 2:
             self.opcion2(cuenta)
         elif op == 3:
             self.opcion3()
         else:
             sys.exit()
      
      
    def opcion1(self,cuenta):      
        nombre = str(input("Ingrese nombre: "))
        cuenta.crearCuenta(input("Ingrese correo electronico: "))
        print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {cuenta.retornaEmail()}")
        print("--------------------------")
        
    def opcion2(self,cuenta):
        x = (input("¿Desea cambiar la contraseña de la cuenta?\n Ingrese si para cambiarla: "))
        if x.lower() == "si":
            cuenta.cambiarContra()
        os.system('pause')
        
    def opcion3(self):
        emails=[]
        print("Se procedera a leer correos electronicos cargados en un archivo csv.")
        with open("emails.csv") as datos:
            print("Emails leidos correctamente.")
            reader = csv.reader(datos)
            for row in reader:
                cuenta = Email()
                print(f"Se utilizara el correo:{str(row[0])} para crear una nueva cuenta.")
                if cuenta.crearCuenta(row[0]):
                    emails.append(cuenta)
            dominio = input("Ingrese dominio a buscar en los objetos creados del archivo: ")
            count = 0
            for email in emails: 
                if dominio==email.getDominio():
                    count+=1
            if count>=1:
              print(f"El dominio {dominio} se encontro {count} veces.")
            else:
                print("------------\nEl dominio no se encontro.\n------------")
