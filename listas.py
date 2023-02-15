compras = ["platanos", "manzanas", "leche"]
articulo1 = (input("Primer articulo que quieres agregar a la compra? "))
articulo2 = (input("Segundo articulo que quieres agregar a la compra? "))
compras.append(articulo2)
compras.append(articulo1)

print("La lista de compras es: ")
for i in compras:
    print(i)

print("El 2do y 3er elemento de la lista son: ")
print(compras[1])
print(compras[2])

posicion = int(input("Teclea el numero de la lista que quieres modificar: "))
modificar = input("Introduce el nuevo parametro: ")
compras[posicion - 1] = modificar

compras.sort()
for n in compras:
    print(n)


