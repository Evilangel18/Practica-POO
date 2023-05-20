class ViajeroFrecuente:
    num_viajero = int
    dni = ""
    nombre = ""
    apellido = ""
    millas_acum = int
    
    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.num_viajero = int(num_viajero)
        self.dni,self.nombre,self.apellido =dni,nombre,apellido 
        self.millas_acum = int(millas_acum)
        
    def getViajero(self):
        return self.num_viajero
    
    def cantidadTotalMillas(self):
        return self.millas_acum
        
    def __radd__(self,millas):
        self.millas_acum+=millas
        return self.millas_acum
    
    def __rsub__(self,millas):
        if millas<=self.millas_acum:
            self.millas_acum-=millas
            print(f"Canje realizado correctamente. El total de sus millas acumuladas actualmente es:{self.millas_acum}\n----------------")
        else:
            print("Error:La cantidad de millas acumuladas no es suficiente para poder realizar un canje!\nIntente nuevamente por favor.\n----------------")
    
    def __eq__(self, otro_viajero):
        if isinstance(otro_viajero, ViajeroFrecuente):
          return self.millas_acum == otro_viajero.millas_acum
        return False