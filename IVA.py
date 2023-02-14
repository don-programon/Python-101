#Programa escrito por Erik Milan. Version 1.0 al 14/02/2023
#Su utilidad es calcular el total de un articulo sumandole el IVA. 
#Dando la posibilidad de visualizar cuanto es el IVA separado del precio y su total

print("Bienvenido a la calculadora de IVA. Diseño por: Erik Milan")
precio = float(input("Introduce el precio sin IVA: "))
porcentaje = float(input("Introduce el porcentaje de IVA a Calcular: "))
iva = float(precio*porcentaje)/100
total = precio + iva
print(f"El calculo del IVA es: {iva: .3f}")
print(f"El total del articulo sumando el IVA es: {total: .3f}")
