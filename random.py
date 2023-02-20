import random

#FUNCION 1
print(dir(random))
x = random.random()
print(x)

#FUNCION 2
y = random.randint(10, 100)
print(y)

#FUNCION 3
frutas = ["manzana", "platano", "kiwi"]
z = random.choice(frutas)
print(z)