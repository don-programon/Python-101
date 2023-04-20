emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
nombres = []
dominios = []
for i in emails:
    a, b = i.split("@")
    nombres.append(a)
    if b not in dominios:    
        dominios.append(b)

print(f"El nombre es: {nombres}") 
print(f"Los dominios son: {dominios}")


