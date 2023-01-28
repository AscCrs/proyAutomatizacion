from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Creacion del objeto que se utilizara para definir el modulo

#Configuracion de la App

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

#Configuracion de las vistas
from project.views import content

app.register_blueprint(content)
