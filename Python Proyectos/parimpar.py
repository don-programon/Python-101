x = int(input("Introduce un numero: "))
y = (int(x) / 2)
print(type(y))

if type(y) == "<class 'float'>":
    print("El numero introducido es impar")

elif type(y) == "<class 'int'>":
    print("El numero introducido es par")



