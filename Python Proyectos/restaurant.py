from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'basedatos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comidas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100))
    precio = db.Column(db.Float)
    descripcion = db.Column(db.String(250))
    activo = db.Column(db.Boolean, default = True)

def __init__(self, nombre, tipo, precio, descripcion, activo):
    self.nombre = nombre
    self.tipo = tipo
    self.precio = precio
    self.descripcion = descripcion
    self.activo = activo

with app.app_context():
    db.create_all()

@app.route("/admin")
def admin():
    plato1 = Comidas("Solomillo", "Carne", 45.9, "Solomillo a la ...", True)
    plato2 = Comidas("Rape", "Pescado", 40.9, "Para dos personas ...", True)
    db.session.add_all([plato1, plato2])
    db.session.commit()
    return "OK"

if __name__=="__main__":
    app.run(debug=True)

#personas = Persona.query.all()
#personas = Persona.query.filter_by(nombre = "Rape")
#s = ""
#for p in personas:
#s = s + p.nombre