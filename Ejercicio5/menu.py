import sys
class Menu:
    opcion = int
    
    def manejador(self,opcion,lista):
        if opcion == 1:
            self.opcion1(lista)
        elif opcion == 2:
            self.opcion2(lista)
        elif opcion == 3:
            self.opcion3(lista)
        elif opcion == 4:
            self.opcion4(lista)
        elif opcion == 5:
            sys.exit()
        
    def opciones(self):
        print("--------------------------\nSeleccione la operacion a realizar:\n--------------------------\n")
        print("|1| Actualizar valor de los vehiculos.")
        print("|2| Dado un valor, mostrar vehiculos con valor de cuota inferior al valor dado.")
        print("|3| Mostrar monto que de debe abonar para poder licitar cada vehiculo.")
        print("|4| Modificar la cantidad cuotas que debe tener pagas para licitar en un plan ingresado.")
        print("|5| Salir.")
        
    def opcion1(self,lista):
        for plan in lista:
            plan.mostrar1()
            plan.modificar_valor(int(input("\nIngrese nuevo valor del vehiculo: ")))
    
    def opcion2(self,lista):
        x=int(input("\nIngrese un valor: "))
        for plan in lista:
            plan.cuota_menor_al_valor_dado(x)
        
    def opcion3(self,lista):
        for plan in lista:
            plan.monto_para_licitar()
            
    def opcion4(self,lista):
        codigo = int(input("Ingrese codigo del plan deseado para modificar la cantidad cuotas que debe tener pagas para licitar: "))
        print(codigo)
        for plan in lista:
            if codigo == plan.getCodigo():
                plan.modificar_cuotas(int(input("Ingrese cantidad nueva de cuotas: ")))
                plan.mostrar()
    
    