from flask import render_template, Blueprint, request, url_for, jsonify
from project.data.models import Sensores_Temp, Variables, Constantes, Calculos

content = Blueprint('content', __name__)

#Routers

@content.route('/')
def home():
    return render_template('test.html')

# @content.route('/<int:id_sensor>/<float:temperatura>/<string:fecha>', methods=['GET'])
# def getData_sensor(id_sensor, temperatura, fecha):
#     inf_sensor = ""
#     return ''

@content.route('/sensores_temp', methods=['GET'])
def get_sensores_temp():
    sensores = Sensores_Temp.query.all()
    return jsonify([{'id_sensor': s.id_sensor, 'temperatura': s.temperatura, 'humedad': s.humedad, 'fecha': s.fecha} for s in sensores])


# @content.route('/')
# def func():
#     return 

# @content.route('/')
# def funcd():
#     return 