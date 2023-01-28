# Script que se encarga de extraer los datos de los sensores 
import os
import glob
import time
from datetime import datetime

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

while True:
    now = datetime.now()
    hora = now.hour
    minuto = now.minute
    print("Temp del sensor 1: "+str(read_temp(0))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
    print("Temp del sensor 2: "+str(read_temp(1))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
    print("Temp del sensor 3: "+str(read_temp(2))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
    print("Temp del sensor 4: "+str(read_temp(3))+" ˚C" + " Hora: " + str(hora) + ":" + str(minuto))
    time.sleep(30)
    print("Pasaron 30 segundos")