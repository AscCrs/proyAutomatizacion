from project.data.models import Sensores_Temp
from project import db
from datetime import datetime

def delete_all_constantes():
    db.session.query(Sensores_Temp).delete()
    db.session.commit()

sensores = [
    Sensores_Temp(num_sensor=1, temperatura=25.2, humedad=60.8, fecha=datetime(2022, 2, 15, 13, 45)),
    Sensores_Temp(num_sensor=2, temperatura=18.9, humedad=40.1, fecha=datetime(2022, 2, 15, 13, 46)),
    Sensores_Temp(num_sensor=3, temperatura=27.6, humedad=55.3, fecha=datetime(2022, 2, 15, 13, 47)),
    Sensores_Temp(num_sensor=4, temperatura=23.1, humedad=45.9, fecha=datetime(2022, 2, 15, 13, 48)),
    Sensores_Temp(num_sensor=1, temperatura=24.3, humedad=59.7, fecha=datetime(2022, 2, 15, 13, 49)),
    Sensores_Temp(num_sensor=2, temperatura=18.5, humedad=40.5, fecha=datetime(2022, 2, 15, 13, 50)),
    Sensores_Temp(num_sensor=3, temperatura=26.8, humedad=56.2, fecha=datetime(2022, 2, 15, 13, 51)),
    Sensores_Temp(num_sensor=4, temperatura=23.8, humedad=44.3, fecha=datetime(2022, 2, 15, 13, 52))
]

def actSensores():
    delete_all_constantes()
    # Verificar si los datos ya existen en la tabla Constantes
    if db.session.query(Sensores_Temp).count() == 0:
        # Insertar los objetos en la base de datos
        db.session.add_all(sensores)
        db.session.commit()
    else:
        print('Elemento duplicado')