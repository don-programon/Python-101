from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

#with app.app_context():
#    db.create_all()

@app.route("/")
def index():
    jon = Persona()
    jon.nombre = "Jon"
    db.session.add(jon)
    maria = Persona()
    maria.nombre = "Maria"
    db.session.add(maria)
    db.session.commit()
    return 'Hola'

@app.route("/sql_all")
def sql_all():
    personas = Persona.query.all()
    #personas = Persona.query.filter_by(nombre = "Maria")
    s = ""
    for p in personas:
        s = s + p.nombre
    return s

@app.route("/sql_todo")
def sql_todo():
    persona = Persona.query.get(4)
    s = persona.nombre
    return s

@app.route("/sql_del")
def sql_del():
    persona = Persona.query.get(2)
    db.session.delete(persona)
    db.session.commit()
    return "Has borrado el registro"

@app.route("/sql_update")
def sql_update():
    persona = Persona.query.get(2)
    persona.nombre = "Jonathan"
    db.session.update(persona)
    db.session.commit()
    return "Has actualizado el registro"

if __name__=="__main__":
    app.run(debug=True)