usuario = input("Introduce tu usuario: ")
prohibido = ["password", "contraseña", "123456"]
validar = False
        
while len(usuario) <= 5:
    print("El usuario debe tener mas de 5 caracteres")
    usuario = input("Introduce tu usuario: ")

if len(usuario) > 5:
    password = input("Introduce tu password: ")

    while len(password) < 6:
        print("El password debe tener mas de 6 caracteres")
        password = input("Introduce tu password: ")
    while password in prohibido:
        print("El password no puede ser esa palabra")
        password = input("Introduce tu password: ")


