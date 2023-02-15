#programa para gestionar invitados de una fiesta
gente = int(input("Cuantos invitados acudiran a la fiesta? "))
max = 5
invitados = []

if gente > max:
    print(f"Lo siento, solo {max} personas pueden acudir a la fiesta")
else:
    for i in range(gente):
        nombre = (input("Introduce el nombre del invitado: "))
        print(f"Has incluido a {nombre} en la fiesta")
        invitados.append(nombre)

print("La lista de invitados es: ")
for x in invitados:
    print(x)

print(f"La cantidad de invitados es: {len(invitados)}")

