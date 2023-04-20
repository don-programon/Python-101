while True:
  pwd1 = input("Introducir tu contraseña: ")
  pwd2 = input("Introducir de nuevo tu contraseña: ")
  if pwd1 == pwd2:
    print("Muy bien. las contraseñas coinciden.")
    break
  print("Las contraseñas no coinciden. Hacerlo de nuevo.")

  
  
i = 1
ch = "*"
while i < 10:
  print(ch*i)
  i= i+2
else:
  print("--------")

i = 9
while i > 0:
  print(ch*i)
  i= i-2