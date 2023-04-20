class Instrumento:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.__coste = precio - 20
    
    def tocar(self):
        print(f"{self.nombre} esta tocando")

#CLASE PIANO HEREDA PROPIEDADES Y METODOS DE LA CLASE INSTRUMENT

class Piano(Instrumento):
    def __init__(self, nombre, tipo, precio, teclas, musico):
        super().__init__(nombre, tipo, precio)
        self.teclas = teclas
        self.musico = musico
    
    def tocar(self):
        print(f"{self.musico.nombre} esta tocando y suena.. DING DING DING")

class Musico:
    def __init__(self, nombre):
        self.nombre = nombre

if __name__ == "__main__":    
    jon = Musico("jon")
    guitarra = Instrumento("Fender", "cuerdas", 100)
    piano1 = Piano("Kurswell", "cuerdas-percusion", 200, 50, jon)

    piano1.tocar()