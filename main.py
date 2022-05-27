#CÓDIGO DE PROCESAMIENTO Y GRAFICACIÓN DE VARIABLES DE UN MOTOR TRIFÁSICO
#Autor: Moises Guillermo Medrano Arias
#Fecha de inicio: 27 de mayo de 2022
#Fecha de finalización:

import serial, serial.tools.list_ports #Library to identify the ports
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from tkinter import Tk,Frame,StringVar,Label,Button,Entry

# ESTABLECER EL PUERTO AL QUE ESTÁ CONECTADO EL ARDUINO

def obtpuerto(): #Obtiene todos los puertos disponibles
    puertos = serial.tools.list_ports.comports() #Variable with the available ports
    return puertos

def encArduino(obtpuerto): #Determinara a que puerto esta conectado el arduino
    commPort = 'None'
    conexiones = len(obtpuerto)

    for i in range(0,conexiones):
        puerto = obtpuerto[i]
        puertostring = str(puerto)

        if 'Arduino' in puertostring:
            separaPuerto = puertostring.split(' ')
            commPort = (separaPuerto[0])
    
    return commPort

puertosEnc = obtpuerto()
conPuerto = encArduino(puertosEnc)

if conPuerto != 'None': #Una vez encontrado el arduino nos imprimira en que puerto esta conectado
    ser = serial.Serial(conPuerto, baudrate = 115200, timeout = 0.2)

    print('Conectado al puerto: ' + conPuerto)
else:
    print('Error de Conexión')



#OBTENER LOS DATOS DEL ARDUINO

#Establecemos las variables que recibimos de arduino
size = 200

voltaje_x = []
voltaje_y = []
voltaje_z = []

corriente_x = []
corriente_y = []
corriente_z = []


i = 0
for i in range(size):
    line = ser.readline(1) #leer la línea de 8 bits/1 byte
    if line:
        string = line.decode()
        
    
