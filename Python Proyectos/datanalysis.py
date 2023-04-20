import requests
url = "https://www.donostia.eus/datosabiertos/catalogo/camaras-trafico/recurso/camarastraficocas.json"
resultado = requests.get(url)

cameras = resultado.text
lista_de_cameras = resultado.json

for i in lista_de_cameras:
    print(type(i))
    if i["Nombre"] == "Ondarreta":
        print("Mi barrio!!!" + i["Latitud"])
    else:
        print(i["Nombre"], i["Latitud"], i["Longitud"])