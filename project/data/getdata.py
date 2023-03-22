# Script que se encarga de extraer los datos de los sensores, aunque funciona 
# de forma independiente a la aplicacion 
import os
import glob
import time
from datetime import datetime
from project.data.models import Sensores_Temp
from project import db

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

def read_temp_raw(pos):
    device_folder = glob.glob(base_dir + '28*')[pos]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(sensor):
    lines = read_temp_raw(sensor)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Ingresar la temperatura de la humedad
hum = 0

def getTemperature(continue_exec):
    while continue_exec:
        try:
            n = 0
            while n < 4:
                now = datetime.now()
                now_str = now.strftime('%Y-%m-%d %H:%M:%S')
                sensor = read_temp(n)
                n += 1
                sens_info = Sensores_Temp(n, sensor, now_str, hum)

                db.session.add(sens_info)
                db.session.commit()

                # print("Temp del sensor 1: "+str(read_temp(0))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
                # print("Temp del sensor 2: "+str(read_temp(1))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
                # print("Temp del sensor 3: "+str(read_temp(2))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
                # print("Temp del sensor 4: "+str(read_temp(3))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
                time.sleep(30)
        except Exception as e:
            print(f"Se produjo un error: {e}")
    print("Deteniendo el proceso en segundo plano ...")
