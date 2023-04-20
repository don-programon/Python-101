import os
import platform

# print(os.environ)
# print(os.getlogin)
# print(os.getcwd)

# path = os.getcwd()
# print(path)
# os.chdir('../')
# path = os.getcwd()
# print(path)

# print(os.name)
# print(platform.uname())
# print(os.getcwd())

os.mkdir("carpeta")
path = os.path.join(os.getcwd(), "carpeta")
print(path)
print(os.path.split(os.getcwd()))


#PARA SUBIR UN NIVEL EN EL DIRECTORIO
os.chdir("../")
#PARA CREAR UN DIRECTORIO EN DONDE SE ESTA TRABAJANDO
os.mkdir("test101")
#OBTIENE LA LISTA DEL DIRECTORIO
s = os.listdir(path)
s = os.getcwd()
print(s)
print(os.listdir(s))



