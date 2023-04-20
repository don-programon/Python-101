
prohibido = ["password", "contraseña", "123456"]
validar_usuario = False
validar_password = False


while validar_usuario == False:
    usuario = input("Introduce tu usuario: ")

    if len(usuario) <= 5:
        print("El usuario debe tener mas de 5 caracteres")

    elif len(usuario) > 5:
        validar_usuario = True
        break

while validar_password == False:
    password = input("Introduce tu password: ")

    if len(password) <= 6:
        print("El password debe tener mas de 6 caracteres")
    
    if password in prohibido:
        print("El password no puede ser esa palabra")
    
    elif len(password) > 6:
        validar_password = True
        break

print("fin")

    

