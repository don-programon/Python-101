num = [3, 97, 126, 3, 56]
#devuelve el codigo ascii de ese numero "print(chr(97))""
#map object
def multiplicar(a):
    return a * 2

def elevacion(a):
    return a * a * a
#map object
print(list(map(map, num)))

print(list(map(multiplicar, num)))
print(list(map(elevacion, num)))
# devuelve el ordinal de una letra
print(ord("a"))