class Viaje:
    def __init__(self, lugar, km):
       self.lugar = lugar
       self.km = 0

class Coche:
    def __init__(self, marca, modelo, fuel, maxfuel, actfuel, consumo, lugar):
        self.marca = marca
        self.modelo = modelo
        self.fuel = fuel
        self.maxfuel = maxfuel
        self.actfuel = 1
        self.consumo = 2
        self.lugar = lugar
    
    def conducir(self):
        y = (Coche.consumo / Viaje.km)

        if self.actfuel < y:
            print (f"Para viajar a {self.lugar.lugar} tienes que llenar el deposito")
        else:
            self.actfuel - y
            print(f"Has llegado a {Viaje.lugar} has consumido {y} litros de combustible")

if __name__ == "__main__":
    bronco = Coche("Ford", "Bronco", "gas", 500)
    madrid = Viaje("Madrid", 100)
    
    bronco.setconducir()
    bronco.getconducir()






        





