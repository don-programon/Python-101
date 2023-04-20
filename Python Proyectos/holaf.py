# def hola():
#     nombre = input("Cual es tu nombre? ")
#     print(f"Hola {nombre}")
    
# if __name__=="__main__":
#     for i in range(3):
#         hola()

#VALORES POR DEFECTO EN VARIABLES DEFINIDAS
# def imprimir(a, b="hello"):
#     print(a, b)

# imprimir("Hola")
# imprimir("Hola", "Kaixo")
# imprimir("Kaixo", "Hola")

# #PASAR TODOS LOS VALORES A LA VARIABLE
# def imprimirNumeros(*args):
#     print(args)

# imprimirNumeros("Hola", "Mundo", "SSSS")

from common.calculadora import *

if __name__=="__main__":
    total = calcular_cuenta(100)
    print(f"Hay que pagar: ${total}")

    total = calcular_cuenta(100, 12)
    print(f"Hay que pagar: ${total}")


