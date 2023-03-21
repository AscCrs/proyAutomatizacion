from flask import render_template, Blueprint, request, url_for
from project.data.models import Sensores_Temp, Variables, Constantes, Calculos

content = Blueprint('content', __name__)

@content.route('/')
def home():
    return render_template('test.html')

@content.route('/calculos')
def test():
    return render_template('calcTest.html')

# @content.route('/<int:id_sensor>/<float:temperatura>/<string:fecha>', methods=['GET'])
# def getData(id_sensor, temperatura, fecha):
#     inf_sensor = ""
#     return ''

# @content.route('/')
# def func():
#     return 

# @content.route('/')
# def funcd():
#     return 