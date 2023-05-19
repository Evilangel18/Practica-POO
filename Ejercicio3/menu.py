from registro import Registro
from dias_por_meses import Menu_meses
import dias_por_meses
import csv
opcion = 0
mes = int(input("Ingrese numero de mes para registrar datos metereologicos:\n|1|Enero\n|2|Febrero\n|3|Marzo\n|4|Abril\n|5|Mayo\n|6|Junio\n|7|Julio\n|8|Agosto\n|9|Septiembre\n|10|Octubre\n|11Noviembre\n|12|Diciembre\n---------------\n"))
menu1 = Menu_meses()
cantidad_dias = menu1.manejador_menu(mes-1)
lista_bidimensional = []
for i in range(cantidad_dias):
    lista_horas = []
    for j in range(24):
        lista_horas.append(None)
    lista_bidimensional.append(lista_horas)
    
with open("datos_meteorologicos.csv") as datos:
    reader = csv.reader(datos)
    for valores in reader:
        dia = int(valores[0])
        hora = int(valores[1])
        temperatura = int(valores[2])
        humedad = int(valores[3])
        presion_atmosferica = int(valores[4])
        registro = Registro(temperatura, humedad, presion_atmosferica)
        lista_bidimensional[dia-1][hora-1] = registro

while opcion != 3:
        print("-----------------------:")
        print("1. Mostrar mínimo y máximo valor de cada variable meteorológica")
        print("2. Calcular temperatura promedio mensual por hora")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1: # Encontrar el mínimo y máximo valor de cada variable meteorológica para cada día y hora        
            temp_min = 99999
            temp_max = 0
            hum_min = 9999
            hum_max = 0
            pres_min = 99999
            pres_max = 0
            for dia in range(cantidad_dias):               
                for hora in range(24):
                 registro = lista_bidimensional[dia][hora]
                 if registro is not None:
                    if registro.temperatura < temp_min:
                            temp_min = registro.temperatura
                    if registro.temperatura > temp_max:
                         temp_max = registro.temperatura
                    if registro.humedad < hum_min:
                         hum_min = registro.humedad
                    if registro.humedad > hum_max:
                            hum_max = registro.humedad
                    if registro.presion_atmosferica < pres_min:
                            pres_min = registro.presion_atmosferica
                    if registro.presion_atmosferica > pres_max:
                            pres_max = registro.presion_atmosferica
        print(f"Maxima temperatura:{temp_max}")
        print(f"Minima temperatura:{temp_min}")
        print(f"Maxima humedad:{hum_max}")
        print(f"Minima humedad:{hum_min}")
        print(f"Maxima presion atmosferica:{pres_max}")
        print(f"Minima presion atmosferica:{pres_min}")