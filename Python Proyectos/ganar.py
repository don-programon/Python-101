jon = (True, False, False, True, False)
maria = (True, True, True, True, True)


if all(jon) == True:
    print("Jon ha ganado todos los partidos")

r =True
for i in maria:
    if i == False:
        r = False
        break
if r == True:
    

# if all(maria) == True:
#     print("Maria ha ganado todos los partidos")