class Coche:
    def __init__(self, marca, modelo, fuel, maxfuel):
    #DECLARAR PRIVADO CON __ Y PROTEGIDO CON _
        self.marca = marca
        self.modelo = modelo
        self.fuel = fuel
        self.maxfuel =  maxfuel 
        self.actfuel = 1
        self.averiado = True

    #SE USA GET PARA MOSTRAR VALORES
    #SE USA SET PARA ASIGNAR VALORES

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

        
if __name__ == "__main__":
    bronco = Coche("Ford", "Bronco", "gas", 100)

    bronco.llenar(50)
    bronco.conducir(20)
    bronco.conducir(31)
    bronco.conducir(1)
    bronco.conducir(1)


    