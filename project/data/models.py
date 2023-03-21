#Archivo que se encargara de generar los modelos para la base de datos
from project import db

class Sensores_Temp(db.Model):
    __tablename__ = 'sensores_temp'
    id_sensor = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=False)
    humedad = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_sensor, temperatura, humedad,fecha):
        self.id_sensor = id_sensor
        self.temperatura = temperatura
        self.fecha = fecha
        self.humedad = humedad

class Variables(db.Model):
    __tablename__ = 'variables'
    id_variables = db.Column(db.Integer, primary_key=True, unique = True)
    ref_ondac = db.Column(db.Float, nullable=False)
    vel_viento = db.Column(db.Float, nullable=False)
    temp_aire = db.Column(db.Float, nullable=False)
    hum_super = db.Column(db.Float, nullable=False)
    altura_cv = db.Column(db.Float, nullable=False)
    desp_cv = db.Column(db.Float, nullable=False)
    long_rugv = db.Column(db.Float, nullable=False)
    ind_af = db.Column(db.Float, nullable=False)
    dens_plant = db.Column(db.Float, nullable=False)

    def __init__(self, ref_ondac, viento, tempair, humsuper, altura, desp, long, ind, dens):
        self.ref_ondac = ref_ondac
        self.vel_viento = viento
        self.temp_aire = tempair
        self.hum_super = humsuper
        self.altura_cv = altura
        self.desp_cv = desp
        self.long_rugv = long
        self.ind_af = ind
        self.dens_plant = dens

class Constantes(db.Model):
    __tablename__ = 'constantes'
    id_constante = db.Column(db.Integer, primary_key=True, unique = True)
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
    coef_cn = db.Column(db.Float, nullable=False)
    cal_latV = db.Column(db.Float, nullable=False)
    rel_macv = db.Column(db.Float, nullable=False)
    rel_mstc = db.Column(db.Float, nullable=False)
    
    sensores_temp_id = db.Column(db.Integer, db.ForeignKey('sensores_temp.id_sensor'), nullable=False)
    sensores_temp = db.relationship("Sensores_Temp", backref = db.backref("sensores_temp", uselist = False))

    constantes_id = db.Column(db.Integer, db.ForeignKey('constantes.id_constante'), nullable=False)
    constantes = db.relationship("Constantes", backref = db.backref("constantes", uselist = False))

    variables_id_var = db.Column(db.Integer, db.ForeignKey('variables.id_variables'), nullable=False)
    variables = db.relationship("Variables", backref = db.backref('variables.id_variables', uselist = False))

    # def __init__(self, calnet, ondac, calsens, calat, coefcn, calatv, relmacv, relmstc, senstemp_id, constid, varid):
    #     self.flujo_calnets = calnet
    #     rad_ondac = ondac
    #     flujo_calsens = calsens
    #     cal_lat = calat
    #     coef_cn = coefcn
    #     cal_latV = calatv
    #     rel_macv = relmacv
    #     rel_mstc = relmstc
    #     sensores_temp_id = senstemp_id
    #     consstantes_id = constid
    #     variables_id_var = varid
