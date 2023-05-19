from ViajeroFrecuente import ViajeroFrecuente 
import csv
import os
import sys
class Menu:
    op = int
    
    def __init__(self):
        self.op=None
    
    def manejoMenu(self,op,viajero,num):
         if op == 1:
             self.opcion1(viajero)
         elif op == 2:
             self.opcion2(viajero,num)
         elif op == 3:
             self.opcion3(viajero,num)
         else:
             sys.exit()
             
    def opcion1(self,viajero):
        return print(f"La cantidad total de millas del viajero son:{viajero.cantidadTotalMillas()} millas.")
          
    def opcion2(self,viajero,num):
        return print(f"Millas acumuladas correctamente!\n Total de millas acumuladas: {viajero.acumularMillas(num)}")
    
    def opcion3(self,viajero,num):
        return viajero.canjearMillas(num)

