def imprimirDiasSemana(*args):
    conteo = 0

    for i in args:
        conteo = conteo + 1
        print(f"{i} es el {conteo} dia de la semana")
        
if __name__=="__main__":

    imprimirDiasSemana("Lunes", "Martes", "Miercoles", "Juernes", "Viernes")
    print("-"*10)

    imprimirDiasSemana("Lunes", "Martes", "Miercoles", "Juernes", "Viernes", "Sabado", "Domingo")





