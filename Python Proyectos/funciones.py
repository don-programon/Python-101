# def ImprimirMensaje(lenguaje):
#     print(f"{lenguaje} es un lenguaje de programacion")  

# def calculo(a):
#     return a + a + a

# if __name__ == '__main__':
#     ImprimirMensaje("Python")
#     ImprimirMensaje("Java")
#     y = calculo(5)
#     print(y)

def restar(a, b):
    return a - b

def sumar(a, b):
    return a + b


if __name__ == '__main__':
    a = int(input("Introducir primer valor: "))
    b = int(input("Introducir segundo valor: "))
    c = restar(a, b)
    d = sumar(a, b)
    print(c)
    print(d)

