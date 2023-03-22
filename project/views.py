from flask import render_template, Blueprint, request, url_for, jsonify
from project.data.models import Sensores_Temp, Variables, VariablesAtm,Constantes, Calculos

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
    return jsonify([{
        'id_temperatura': s.id_temperatura, 
        'num_sensor': s.num_sensor,
        'temperatura': s.temperatura, 
        'humedad': s.humedad, 
        'fecha': s.fecha
        } for s in sensores])

@content.route('/calculos', methods=['GET'])
def get_calculos():
    calculos = Calculos.query.all()
    return jsonify([{
        'id_calculo': c.id_calculos,
        'flujo_calnet': c.flujo_calnet,
        'rad_ondac': c.rad_ondac,
        'flujo_calsens': c.flujo_calsens,
        'cal_lat': c.cal_lat,
        'coef_cn': c.coef_cn,
        'cal_latV': c.cal_latV
    }for c in calculos])

@content.route('/variables_atm', methods=['GET'])
def get_variables_atm():
    variablesatm = VariablesAtm.query.all()
    return jsonify([{
        'id_var_atm': varatm.id_var_atm,
        'ref_ondac': varatm.ref_ondac,
        'vel_viento': varatm.vel_viento,
        'temp_aire': varatm.temp_aire
    } for varatm in variablesatm])

@content.route('/variables', methods=['GET'])
def get_variables():
    variables = Variables.query.all()
    return jsonify([{
        'id_variable': var.id_variables,
        'hum_super': var.hum_super,
        'altura_cv': var.altura_cv,
        'desp_cv': var.altura_cv,
        'long_rugv': var.long_rugv,
        'ind_af': var.ind_af,
        'm_airecv': var.m_airecv,
        'sat_tempcv': var.sat_tempcv
    } for var in variables])

@content.route('/constantes', methods=['GET'])
def get_constantes():
    constantes = Constantes.query.all()
    return jsonify([{
        'id_constante': c.id_constante,
        'temp_const': c.temp_const,
        'dens_aire': c.dens_aire,
        'calor_especif': c.calor_especif
    } for c in constantes])

# @content.route('/')
# def func():
#     return 

# @content.route('/')
# def funcd():
#     return 