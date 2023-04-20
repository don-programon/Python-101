class Coche:
    def __init__(self, marca, modelo, fuel, maxfuel):
    #DECLARAR PRIVADO CON __ Y PROTEGIDO CON _
        self.marca = marca
        self.modelo = modelo
        self.fuel = fuel
        self.maxfuel =  maxfuel 
        self.actfuel = 1
        self.averiado = True

    def conducir(self, value):
        if self.actfuel <= 0:
            print("Te has acabado la gasolina. No puedes viajar")
        else:
            self.actfuel = self.actfuel - value
            print(f"Estas conduciendo... has consumido {value} litros de gasolina y te quedan {self.actfuel}")
    
    def llenar(self, value):
        if self.actfuel == self.maxfuel or self.actfuel + value >= self.maxfuel:
            print("Tu tanque esta lleno, no puedes llenar mas")
        elif self.actfuel < self.maxfuel:
            self.actfuel = self.actfuel + value
            print(f"Has recargado {value} litros de gasolina y tienes {self.actfuel} ")

class Camion(Coche):
    def __init__(self, marca, modelo, fuel, maxfuel, cabina):
        super().__init__(marca, modelo, fuel, maxfuel)
        self.cabina = cabina
        self.despierto = True
    
    def dormir(self):
        self.despierto = False
        print(f"El conductor del {self.modelo} esta dormido")
    
    def despertar(self):
        self.despierto = True
        print(f"El conductor del {self.modelo} esta despierto")
    
    def conducir(self, value):
        if self.actfuel <= 0:
            print("Te has acabado la gasolina. No puedes viajar") 
        else:
            self.actfuel = self.actfuel - value
            print(f"Estas conduciendo... has consumido {value} litros de gasolina y te quedan {self.actfuel}")
        
        if self.despierto == False:
            print(f"El conductor del {self.modelo} esta dormido. No puedes viajar")

        

        
if __name__ == "__main__":
    bronco = Coche("Ford", "Bronco", "gas", 100)
    encava = Camion("Chevrolet", "Encava", "diesel", 200, "grande")
    
    encava.llenar(50)
    encava.dormir()
    encava.conducir(3)
    encava.despertar()
    encava.conducir(5)

    # bronco.llenar(50)
    # bronco.conducir(20)
    # bronco.conducir(31)
    # bronco.conducir(1)
    # bronco.conducir(1)