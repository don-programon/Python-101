from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comidas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    tipo = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)
    activo = db.Column(db.Boolean, default=True)

    def __init__(self, nombre, descripcion, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio = precio
        self.activo = True

with app.app_context():
    db.create_all()

@app.route("/rellenar")
def rellenarBD():
    plato1 = Comidas("Solomillo","Carne", "A la parrilla", 29.5)
    plato2 = Comidas("Rape", "Pescado", "En Salsa", 75.9)
    db.session.add_all([plato1, plato2])
    db.session.commit()
    return "OK"

@app.route("/comidas")
def comidas():

    lista_comidas = Comidas.query.all()
    return render_template("comidas.html", comidas = lista_comidas)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form.get("txtNombre")
        tipo = request.form.get("txtTipo")
        descripcion= request.form.get("txtDescripcion")
        precio = float(request.form.get("txtPrecio"))
        comida = Comidas(nombre, tipo, descripcion, precio)
        db.session.add(comida)
        db.session.commit()
        return "El plato" + comida.nombre + "ha sido agregado al menu"
    else:
        return render_template("agregar.html")

if __name__=="__main__":
    app.run(debug=True)