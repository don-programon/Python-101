# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."

# texto = texto.replace("Pitón", "Python")
# texto = texto.replace("Bill Gates en 1960", "Guido Van Rossum en 1991")
# texto = texto.replace("difícil", "facil")
# print(texto)

texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil  "

#CONTAR LAS VECES QUE APARECE LA PALABRA PYTHON EN TEXTO
contar = texto.count("Python") + texto.count("python")
print(f"Las veces que se repite son: {contar}")

#BUSCAR PALABRAS ESPECIFICAS
buscar = texto.find("Python")
buscar2 = texto.find("Python", 50, len(texto))
print(f"La primera palabra esta en: {buscar} y la segunda en: {buscar2}")

#ENCONTRAR UNA PALABRA CON IF/IN
if "codigo" in texto:
    print("La palabra codigo si esta en el texto")
else:
    print("La palabra codigo no esta en el texto")

#REEMPLAZAR
texto = texto.replace("Python", "PYTHON")
texto = texto.replace("python", "PYTHON")
print(texto)

#QUITAR ESPACIOS A LA IZQUIERDA/DERECHA
print("X" + texto.lstrip() + "X")
print("X" + texto.rstrip() + "X")

#CAMBIAR LAS MAYUSCULAS POR MINUSCULAS
print(texto.swapcase())







