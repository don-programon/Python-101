# nombres = ["Jon", "Maria", "Juan", "Javier"]
# #LIST COMPREHENTION
# lista = [nombre for nombre in nombres if nombre[0] =="J"]

# for nombre in nombres:
#     if nombre[0] == "J":
        

numeros = [3, 54, -12, 4, -67, 99, -120]
positivos = [positivo for positivo in numeros if positivo>0]
negativos = [negativo for negativo in numeros if negativo<0]
print(positivos)
print(negativos)
