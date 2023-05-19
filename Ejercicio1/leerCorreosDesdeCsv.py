from Email import Email
import csv
print("Se procedera a leer correos electronicos cargados en un archivo csv.")
with open("emails.csv") as datos:
        print("Emails leidos correctamente.")
        reader = csv.reader(datos)
        for row in reader:
            print(f"Se utilizara el correo:{str(row[0])} para crear una nueva cuenta.")
            crear = Email()
            crear.crearCuenta(row[0])
            
        