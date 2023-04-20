Modo = str(input("Teclea A si quieres: Kilos a Libras // Teclea B si quieres Libras a Kilos"))
Peso = float(input("Introduce el peso: "))
if Modo == str("A"):
    Peso = (Peso*2.225)
    print(f"La conversion de Kilos a Libras es " + str(Peso))
elif Modo == str("B"):
    Peso = (Peso/2.225)
    print(f"La conversion de Libras a Kilos es " + str(Peso))
else:
    print("Estas tecleando una opcion incorrecta")
