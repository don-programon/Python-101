alumnos = ["carlos", "erik", "ramon"]
total = 0

print("Control de asistencia de clase: ")

for i in alumnos:
    asistencia = (input("Ha venido " + i + " ? y/n: "))   
    if asistencia == "y":
        total = total + 1

print (f"La asistencia de hoy es: {total}")
