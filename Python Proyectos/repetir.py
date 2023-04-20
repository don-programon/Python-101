#Programa para repetir un input 10 veces

# nombre = input("Cual es tu nombre? ")
# for i in range (10):
#     print(str(i) + nombre)

#Programa para contar
rep = int(input("Cuantas veces quieres contar? "))
conteo = str(input("Teclea up para contar en positivo // Teclea down para contar en negativo: "))

if conteo == "up":
    for i in range(rep):
        print(i+1)
elif conteo == "down":
    for i in range(rep, 0, -1):
        print(i)

