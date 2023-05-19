class Ventana:
    x_izq_sup = int
    y_izq_sup = int
    x_der_inf =  int
    y_der_inf =  int
    
    def __init__(self, titulo, x_izq_sup= 0,y_izq_sup = 0,x_der_inf=500,y_der_inf=500):  
        self.titulo = titulo
        self.x_izq_sup = x_izq_sup
        self.y_izq_sup = y_izq_sup
        self.x_der_inf = x_der_inf
        self.y_der_inf = y_der_inf
       
    def mostrar(self):
        return print(f"Ventana {self.titulo}:\nCoordenadas del vértice superior izquierdo:({self.x_izq_sup},{self.y_izq_sup})\nCoordenadas del vértice inferior derecho:({self.x_der_inf},{self.y_der_inf})")
    
    def getTitulo(self):
        return self.titulo
    
    def alto(self):
        xalto = self.x_der_inf - self.x_izq_sup
        return xalto
    
    def ancho(self):
        xancho = self.y_der_inf - self.y_izq_sup
        return xancho
    
    def moverDerecha(self,unidades=1):
        self.x_der_inf += unidades
        self.x_izq_sup += unidades
    
    def moverIzquierda(self,unidades=1):
        self.x_der_inf -= unidades
        self.x_izq_sup -= unidades
    
    def bajar(self,unidades=1):
        self.y_der_inf-=unidades
        self.y_izq_sup-=unidades
        
    def subir(self,unidades=1):
        self.y_der_inf+=unidades
        self.y_izq_sup+=unidades

    