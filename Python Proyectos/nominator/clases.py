class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def calcular_salario(self, empleados):
        print("CALCULANDO NOMINAS")
        print("==================")
        if self.lenguaje == "python":
            self.salario = self.salario * 1.2
        elif self.lenguaje == "java":
            self.salario = self.salario * 1.3

        empleados = []
        for empleado in empleados:
            print(f"Nomina para {empleado.nombre} - {empleado.lenguaje}")
            print()

    
    
    




