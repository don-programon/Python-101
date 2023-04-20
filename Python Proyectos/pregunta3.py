#DEFINIMOS UN METODO CON VALOR ALTURA POR DEFECTO
def calcular_area(base, altura = 3): 
    area = base * altura
    return area

#IMPRIMIMOS PARA PROBAR QUE ESTA TOMANDO EL VALOR
print(calcular_area(10, 4))
print(calcular_area(10))
print(calcular_area(20, 6))

#PEDIMOS AL USUARIO LOS VALORES PARA SUSTITUIRLOS EN EL METODO E IMPRIMIR RESULTADO
area = float(input("Cual es la base?"))
altura = float(input("Cual es la altura"))
print(calcular_area(area, altura))



