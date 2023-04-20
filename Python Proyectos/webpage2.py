from flask import Flask, request, render_template, redirect, url_for
from datetime import date

app = Flask(__name__)

class Coches:
    def __init__(self, id, modelo, precioc, preciof, image, image2):
        self.id = id
        self.modelo = modelo
        self.precioc = precioc
        self.preciof = preciof
        self.image = image
        self.image2 = image2



listaCoches = []

peugeot = Coches(1, "Peugeot 308", 22900, 19900, "peugeut308_1.png", "peugeot308_2.jpg")
audi = Coches(2, "Audi A5", 25900, 23900, "audia5.png", "audia5_2.jpg")
renault = Coches(3, "Renault Megane", 12300, 0, "megane.png", "megane_2.jpg")

listaCoches.append(peugeot)
listaCoches.append(audi)
listaCoches.append(renault)

@app.route("/coches")
def personas():
    return render_template("coches.html", coches = listaCoches)

@app.route("/coche/<int:id>")
def dinamic(id):
    for coche in listaCoches:
        if id == coche.id:
            return render_template("coche.html", coche = coche)
    else:
        #REDIRECCIONANDO CON REDIRECT
        return redirect("/")
        # REDIRECCIONANDO CON URL FOR...
        # return redirect(url_for("hola"))

@app.route("/form1", methods=["GET", "POST"])
def form1():
    datos = ""
    if request.method == "POST":
        nombre = request.form["txtNombre"]
        email = request.form["txtEmail"]
        mensaje = request.form["txtMsj"]
        hoy = date.today()
        datos = "NOMBRE: " + nombre + " - " + "EMAIL: " + email + " - " + "MENSAJE: " + mensaje + " - " + "FECHA: " + hoy.strftime("%Y-%m-%d")
        with open('datos.txt', 'a') as f:
            f.write(datos)
            f.write('\n')
        return "GRACIAS POR TU MENSAJE: " + nombre
    else:
        return render_template("form1.html")

if __name__=="__main__":
    app.run(debug=True)