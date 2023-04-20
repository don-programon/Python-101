texto = "Pitón es un lenguaje de programación. Pitón está Usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón es fácil de usar."

print("\n")
print(texto.replace("Pitón", "Python"))
print("\n")
print(texto.upper())
print("\n")
s = texto.split(" ")
print(sorted(s))
print("\n")
for i in s:
    print(i[0])
