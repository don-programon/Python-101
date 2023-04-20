
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def hablar(self):
        print(f"Hola, soy {self.nombre} y mi edad es {self.edad}")

personas = []

if __name__ == "__main__":
    nombre = input("Introducir un nombre de usuario: ")
    edad = input("Introducir la edad: ")

    persona = Persona(nombre, edad)
    personas.append(persona)

print(personas)

