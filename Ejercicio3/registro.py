class Registro:
    temperatura = int
    humedad = int
    presion_atmosferica = int
    
    def __init__(self, temperatura, humedad, presion_atmosferica):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion_atmosferica = presion_atmosferica
    
    
    
    
    #Cada una hora(24hs) todos los dias del mes(30dias)  
    #Se genera un archivo por cada mes.
    