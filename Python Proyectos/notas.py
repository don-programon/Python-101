lista_notas = [5, 6, 4, 3, 9, 9, 10]
aprobado = True

for i in lista_notas:
    if i < 5:
        aprobado = False
        break
print(f"La clase aprobo? {aprobado}")