
# DEFINIMOS CLASE PRINCIPAL CON SUS ATRIBUTOS
class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

# DEFINIMOS CLASE PERRO QUE HEREDA DE ANIMAL CON SUS PROPIOS METODOS
class Perro(Animal):
    def __init__(self, nombre, patas, raza):
        super().__init__(nombre, patas)
        self.nombre = nombre
        self.patas = patas
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} esta ladrando. WOOF! WOOF!")
    
    def correr(self):
        print(f"{self.nombre} esta corriendo como loco!")

# DEFINIMOS CLASE PAJARO QUE HEREDA DE ANIMAL CON SUS PROPIOS METODOS
class Pajaro(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
        self.nombre = nombre
        self.patas = patas
    
    def tweet(self):
        print(f"{self.nombre} esta haciendo ruido. TWEET! TWEET!")
    
    def volar(self):
        print(f"{self.correr} esta volando hacia el infinito!")

# EN LA APLICACION PRINCIPAL PEDIMOS AL USUARIO PARA INSTANCIAR UN PERRO
if __name__ == "__main__":
    
    nombre = input("Introducir un nombre de perro: ")
    patas = input("Introducir patas: ")
    raza = input("Introducir la raza: ")
    perro = Perro(nombre, patas, raza)
    print(f"NOMBRE: {perro.nombre}, PATAS: {perro.patas}, RAZA: {perro.raza}")

# LLAMAMOS A LOS METODOS DE PERRO PARA PROBAR QUE FUBNCIONAN
    perro.ladrar()
    perro.correr()
