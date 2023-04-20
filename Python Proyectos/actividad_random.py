import random
# x = random.randint(12, 18)

# if x == 15:
#     print("El numero es 15!")

alumnos = ["Jon", "Maria", "Juan", "Asier"]
z = random.choice(alumnos)
print(z)

if z == "Maria" or z == "Juan":
    print("Maria y Juan no estan en clase")

else:
      print("Asier y jon estan en clase")


