with open("a1.txt", "r") as f:
    s = f.read()
s = s.upper()
print(s)

with open("a1.txt", "w") as f:
    f.write(s)
        

