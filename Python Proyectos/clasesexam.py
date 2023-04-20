class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def comprobar_upper(self):
        if self.nombre == self.nombre.upper():
            print(f"{self.nombre} tiene mayuscula")
        else:
            print(f"{self.nombre} esta en minuscula")

    def comprobar_precio(self):
        if self. precio > 10:
            print(f"El precio de {self.nombre} es mayor que 10")
        else:
            print(f"El precio de {self.nombre} es menor que 10")

        

class vaqueros(Producto):
    def __init__(self, nombre, precio, stock, talla):
        super().__init__(nombre, precio, stock)
        self.talla = talla

class Libro(Producto):
    def __init__(self, nombre, precio, stock, autor):
        super().__init__(nombre, precio, stock)
        self.autor = autor

class Camiseta(Producto):
    def __init__(self, nombre, precio, stock, color):
        super().__init__(nombre, precio, stock)
        self.color = color







