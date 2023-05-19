from Email import Email 
nombre = str(input("Ingrese nombre: "))
cuenta = Email()
cuenta.crearCuenta(input("Ingrese correo electronico: "))
print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {cuenta.retornaEmail()}")
print("--------------------------")
x = (input("¿Desea cambiar la contraseña de la cuenta?\n Ingrese si para cambiarla: "))
if x.lower() == "si":
    cuenta.cambiarContra()