class PlanAhorro:
    codigo_plan = int
    modelo = ""
    version = ""
    valor_vehiculo = int
    cant_cuotas = int
    cuotas_pagas = int
    
    def __init__(self,codigo_plan,modelo,version,valor_vehiculo,cant_cuotas,cuotas_pagas):
        self.codigo_plan = int(codigo_plan)
        self.modelo = str(modelo)
        self.version = str(version)
        self.valor_vehiculo = int(valor_vehiculo)
        self.cant_cuotas = int(cant_cuotas)
        self.cuotas_pagas = int( cuotas_pagas)
    
    def mostrar(self):
        print(f"Codigo de plan:{self.codigo_plan} |Modelo {self.modelo}, version: {self.version} |Valor vehiculo:{self.valor_vehiculo}| Cantidad de cuotas:{self.cant_cuotas}|Cuotas para licitar:{self.cuotas_pagas}")

    def mostrar1(self):
        print(f"Codigo de plan:{self.codigo_plan} | Modelo: {self.modelo} | Version: {self.version}")

    def modificar_valor(self,valor):
        self.valor_vehiculo = valor
    
    def valorCuota(self):
        return (self.valor_vehiculo / self.cant_cuotas) + self.valor_vehiculo * 0.10
    
    def cuota_menor_al_valor_dado(self,dado):
        valor = self.valorCuota()
        if valor < dado:
            self.mostrar1()
    
    def monto_para_licitar(self):
        return print(f"El monto que se debe abonar para licitar el vehiculo {self.modelo}|{self.version} es de: ${round(self.cuotas_pagas * self.valorCuota(),2)}")

    def getCodigo(self):
        return self.codigo_plan
    
    def modificar_cuotas(self,cuotas):
        self.cuotas_pagas = cuotas
        
