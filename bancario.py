#PROGRAMA PARA LLEVAR CONTROL DE TRANSACCIONES
saldo = float(input("Cual es tu saldo? "))
transacciones = []

while saldo > 0:
    transaccion = float(input("De cuanto es la transaccion? "))
    tipo = (input("Teclea R para retiro o I para hacer un ingreso: "))

    if tipo == "r" or tipo == "R":
        saldo = saldo - transaccion
        transacciones.append([transaccion, tipo])
        print(f"Tu saldo actual es: {saldo}")

    if tipo == "i" or tipo == "I":
        saldo = saldo + transaccion
        transacciones.append([transaccion, tipo])
        print(f"Tu saldo actual es: {saldo}")

if saldo == 0:
    for t in transacciones:
        print(f"Tu... {t[]}")

        #for i in t:
            #print(i, end="")






