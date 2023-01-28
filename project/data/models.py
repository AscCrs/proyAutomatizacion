#Archivo que se encargara de generar los modelos para la base de datos
from project import db

class Sensores_Temp(db.Model):
    __tablename__ = 'sensores_temp'
    id_sensor = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_sensor, temperatura, fecha):
        self.id_sensor = id_sensor
        self.temperatura = temperatura
        self.fecha = fecha

class Variables(db.Model):
    __tablename__ = 'variables'
    id_variables = db.Column(db.Integer, primary_key=True)
    ref_ondac = db.Column(db.Float, nullable=False)
    vel_viento = db.Column(db.Float, nullable=False)
    temp_aire = db.Column(db.Float, nullable=False)
    hum_super = db.Column(db.Float, nullable=False)
    altura_cv = db.Column(db.Float, nullable=False)
    desp_cv = db.Column(db.Float, nullable=False)
    long_rugv = db.Column(db.Float, nullable=False)
    ind_af = db.Column(db.Float, nullable=False)
    dens_plant = db.Column(db.Float, nullable=False)

    def __init__(self, ref_ondac, vel_viento, temp_aire, hum_super, altura):
        self.ref_ondac = ref_ondac

class Constantes(db.Model):
    __tablename__ = 'constantes'
    id_constante = db.Column(db.Integer, primary_key=True)
    temp_const = db.Column(db.Float, nullable=False)
    dens_aire = db.Column(db.Float, nullable=False)
    calor_especif = db.Column(db.Float, nullable=False)

    def __init__(self, temp, dens, calesp):
        self.temp_const = temp
        self.dens_aire = dens
        self.calor_especif = calesp

class Calculos(db.Model):
    __tablename__ = 'calculos'
    id_calculos = db.Column(db.Integer, primary_key=True)
    flujo_calnet = db.Column(db.Float, nullable=False)
    rad_ondac = db.Column(db.Float, nullable=False)
    flujo_calsens = db.Column(db.Float, nullable=False)
    cal_lat = db.Column(db.Float, nullable=False)
    coef_cn = db.Column(db.Double, nullable=False)
    cal_latV = db.Column(db.Float, nullable=False)
    rel_macv = db.Column(db.Float, nullable=False)
    rel_mstc = db.Column(db.Float, nullable=False)
    id_sensor = db.Column(db.Integer, db.ForeignKey('sensores_temp.id_sensor'), nullable=False)
    id_const = db.Column(db.Integer, db.ForeignKey('constantes.id_constante'), nullable=False)
    id_variables = db.Column(db.Integer, db.ForeignKey('variables.id_variables'), nullable=False)