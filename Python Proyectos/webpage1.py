from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class Empleado:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

listaPersonas = ["Erik", "Walter", "Arthur"]
listaEmpleados = []

erik = Empleado("Erik", "Milan", 35)
walt = Empleado("Walter", "White", 56)
arthur = Empleado("Arthur", "Smith", 27)

listaEmpleados.append(erik)
listaEmpleados.append(walt)
listaEmpleados.append(arthur)

@app.route("/")
def hola():
    return render_template("index.html", empleado=erik)

@app.route("/adios")
def adios():
    return app.send_static_file("aboutus.html")

@app.route("/personas")
def personas():
    return render_template("personas.html", empleados = listaEmpleados)

@app.route("/dinamica/<int:id>")
def dinamic(id):
    if id==10:
        return "Has selecionado dinamica 10!"
    else:
        #REDIRECCIONANDO CON REDIRECT
        return redirect("/")
        # REDIRECCIONANDO CON URL FOR...
        # return redirect(url_for("hola"))
    
if __name__=="__main__":
    app.run(debug=True)