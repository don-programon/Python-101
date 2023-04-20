
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.raza = raza
        self.edad = int(edad)

    def presentar(self):
        print(f"{self.nombre} tiene {self.edad} años y es un {self.raza} ")
    
    def ladrar(self):
        if self.edad < 10:
            print(f"{self.nombre} esta LADRANDO")
        else:
            print(f"{self.nombre} esta ladrando")
        

    
if __name__ == "__main__":
    # PARA DECLARAR OBJETOS
    # cookie = Perro("Cookie", 4, "Border Collie")
    # tobby = Perro("Toby", 6, "Cacri")
    perros = []
    contador = 0
    
    while contador < 2:
        nombre = input("Introducir un nombre de perro: ")
        edad = input("Introducir la edad: ")
        raza = input("Introducir la raza: ")
        contador = contador + 1
        perro = Perro(nombre, edad, raza)
        perros.append(perro)

    for i in perros:
        i.presentar()
        i.ladrar()

    





