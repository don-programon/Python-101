from common.calculadora import *

if __name__=="__main__":

    a = float(input("Introduce el primer numero: "))
    b = float(input("Introduce el segundo numero: "))
   
    print(sumar(a, b))
    print(restar(a, b))
    print(multiplicar(a, b))
    print("%.2f" % dividir(a, b))