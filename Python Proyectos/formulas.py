def distcal():
    t = float(input("Introduce el tiempo: "))
    v = float(input("Introduce la velocidad: "))
    d = v * t
    print(f"La distancia es {d}")  

def velcal():
    t = float(input("Introduce el tiempo: "))
    d = float(input("Introduce la distancia: "))
    v = d / t
    print(f"La velocidad es {v}")

def timecal():
    d = float(input("Introduce la distancia: "))
    v = float(input("Introduce velocidad: "))
    t = d / v
    print(f"La distancia es {t}")  

if __name__=="__main__":
        
    print("Bienvenido a la calculadora de tiempo, velocidad, distancia")
    opcion = input("¿Que deseas calcular? (d,t,v) Teclea la opcion: ")

    if opcion == "d":
        distcal()

    if opcion == "v":
        velcal()
    
    if opcion == "t":
        timecal()
    
        
    








