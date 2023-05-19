dias_por_mes = [31,2,31,30,31,30,31,31,30,31,30,31] 
def retornar_dias(num):
    return dias_por_mes[num]

class Menu_meses:
    op= int
    
    def __init__(self):
        self.op=None
    
    def manejador_menu(self,op):
            return retornar_dias(op)
    
