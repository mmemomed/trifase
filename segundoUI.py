import serial, serial.tools.list_ports #Library to identify the ports
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from tkinter import Tk,Frame,StringVar,Label,Button,Entry

def obtpuerto(): #Obtiene todos los puertos disponibles
    puertos = [port.device for port in serial.tools.list_ports.comports() ] #Variable with the available ports
    return puertos

def encArduino(obtpuerto): #Determinara a que puerto esta conectado el arduino
    commPort = 'Ninguno'
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
    ser = serial.Serial(conPuerto, baudrate = 115200, timeout = 200)
    print('Conectado al puerto: ' + conPuerto)
else:
    print('Error de Conexión')

