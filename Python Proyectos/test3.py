a = 10
print(id(a))

b = 11
isinstance(a, int)
type(b)

c = int(input("Introduce valor de C "))
if c in [10,11]:
    print("C es igual a "+ str(c))

d = 10
if d > 10:
    print(f"La variable A con valor {d} es mas que 10. ")
else:
    print(f"La variable A {d} es menor o igual")
