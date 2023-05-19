from ViajeroFrecuente import ViajeroFrecuente
from menu import Menu
from pruebas import buscarviajero as buscar
import csv
import sys

menu=Menu()

with open('viajeros.csv',"r+") as datos:
            reader = csv.reader(datos)
            writer = csv.writer(datos)
            lista_viajeros = []
            for fila in reader:
                num_viajero,dni,nombre,apellido,millas_acum = int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]) 
                viajero = ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
                lista_viajeros.append(viajero)

x=int(input("Bienvenido!\nIngrese su numero de viajero:"))
viajero_encontrado = buscar(lista_viajeros,x)

while viajero_encontrado!=None:
    op= int(input('Ingrese la operacion que desea realizar:\n|1|Consultar cantidad de millas.\n|2|Acumular Millas.\n|3|Canjear Millas.\n|4|Salir\n'))
    if op == 1: #or 2 or 3:
        menu.manejoMenu(op,viajero_encontrado,0)
    elif op == 2:
        millas=int(input("Ingrese cantidad de millas para acumular: "))
        menu.manejoMenu(op,viajero_encontrado,millas)
    elif op==3:
        millas=int(input("Ingrese cantidad de millas que desea canjear: "))
        menu.manejoMenu(op,viajero_encontrado,millas)    
    else:
        sys.exit()
