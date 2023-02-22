#PROGRAMA PARA LLEVAR CONTROL DE TRANSACCIONES BANCARIAS
saldo = float(input("Cual es tu saldo? "))
media = 0
lista1 = []
conteo = 0

#HACEMOS QUE EL PROGRAMA REPITA TRANSACCIONES MIENTRAS EL SALDO SEA MAS QUE 0
while saldo > 0:
    transaccion = float(input("De cuanto es la transaccion? "))
    tipo = (input("Teclea R para retiro o I para hacer un ingreso: "))

#FUNCION PARA RETIRAR DINERO
    if tipo == "r" or tipo == "R":
        saldo = saldo - transaccion
        conteo = conteo + 1
        tipo = "- Retiro"
        lista1.append([- transaccion, tipo])
        print(f"Tu saldo actual es: {saldo}")
        
    if saldo - transaccion < 0:
        print("Tu saldo es insuficiente")

#FUNCION PARA INGRESAR DINERO
    elif tipo == "i" or tipo == "I":
        saldo = saldo + transaccion
        conteo = conteo + 1
        tipo = "- Ingreso"
        lista1.append([transaccion, tipo])
        print(f"Tu saldo actual es: {saldo}")

#DAMOS UN INFORME DE LAS TRANSACCIONES HECHAS Y LA MEDIA
if saldo == 0:
    for i in lista1:
        print (i[0], i[1])
    
    for i in lista1:
        media = (media + i[0]) / conteo
    
    print (f"El total de transacciones hechas es: {conteo}")
    print (f"La media de transacciones hechas es: {media}")



   
   






