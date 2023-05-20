from ViajeroFrecuente import ViajeroFrecuente

def buscarviajero(lista,num):
    for viajero in lista:
        if viajero.getViajero() == num:
            print("Numero de viajero encontrado con exito!\n---------------------")
            return viajero
    print("Numero de viajero no encontrado!\n----------------------")   
            