from is_isbn.is_isbn import is_isbn
contador = 0
y = ""

with open("a1.txt", "r") as f:
    lista = f.readlines()

for i in lista:
    x = is_isbn(i)
    contador = (contador + 1)

    if x == True:
        y = ("Correcto")
    elif x == False:
        y = ("Incorrecto")

    print(f"El ISBN {contador}: {i} es: {y}")

     