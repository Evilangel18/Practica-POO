from plan_ahorro import PlanAhorro as plan
from menu import Menu
import csv
import sys
instancias = []

with open("planes.csv","r") as datos:
    reader = csv.reader(datos,delimiter = ';')
    for fila in reader:
        a = plan(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        instancias.append(a)    
          
if __name__=="__main__":
    xmenu = Menu()
    x = 0
    while x == 0:
        xmenu.opciones()
        opcion=int(input("Ingrese opcion:"))
        xmenu.manejador(opcion,instancias)
