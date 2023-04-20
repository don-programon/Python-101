acciones = {"AENA":143.75, "BBVA":6.34, "REP":14.22, "SAN":3.324}
print(acciones["BBVA"])

acciones.update({"OHLA":0.518, "ANE":34.32, "TEF":3.811})
print(acciones)

total = 0
for key, value in acciones.items():
    if key != "SAN":
        total = total + value

print(f"El total de las acciones: {total}")