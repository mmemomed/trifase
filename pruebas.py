'''
import serial, serial.tools.list_ports #Library to identify the ports
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from itertools import count

#ESTABLECIMIENTO DE FUNCIONES
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


#CONEXIÓN A ARDUINO
puertosEnc = obtpuerto()
conPuerto = encArduino(puertosEnc)

if conPuerto != "None": #Una vez encontrado el arduino nos imprimira en que puerto esta conectado
    ser = serial.Serial(conPuerto, baudrate = 115200, timeout = 0.2)

    print('Conectado al puerto: ' + conPuerto)
else:
    print('Error de Conexión')


#LECTURA DE VARIABLES Y GRÁFICAS
temperatura = [] #lista para almacenar los datos de voltaje
humedad = [] #Lista para almacenar los datos de corriente
tiempo = [] #Lista para almacenar los datos de tiempo 


'''

'''
while True:    
    puertosEnc = obtpuerto()
    conPuerto = encArduino(puertosEnc)
    if conPuerto == 'None':     #ROMPE EL CICLO SI SE DESCONECTA EL ARDUINO
        break
    linea = ser.readline()
    string = linea.decode()
    if string != '':
        sep = string.split(',')
        pvar = float(sep[1])
        svar = float(sep[2])
        tvar = float(sep[0])
        humedad.append(pvar)
        temperatura.append(svar)


plt.show()





import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()

import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from itertools import count

x1 = []
x2 = []
y = []
z = []
 
index = count()

def ani1(i):
    x1.append(next(index))
    y.append(random.randint(0,10))
    z.append(random.randint(0,5))
    plt.cla()
    plt.plot(x1,y)
    plt.plot(x1,z)
    plt.xlabel("X")
    plt.ylabel("Y/Z")
    plt.tight_layout()


anim1 = FuncAnimation(plt.gcf(), ani1, interval = 1000)

plt.show()
'''
import serial 
import matplotlib.pyplot as plt
import numpy
from drawnow import *

temp = []
humedad=[]
plt.ion()
cnt = 0
ser = serial.Serial('com6', 9600)

def makeFig():
    plt.ylim(0,80)
    plt.title('Mis datos desde el Arduino')
    plt.grid(True)
    plt.ylabel('Temperatura C')
    plt.plot(temp, 'ro-', label = 'Grados C')
    plt.legend(loc = 'upper left')
    plt2 = plt.twinx()
    plt.ylim (0,100)
    plt2.plot(humedad,'b^-', label = 'Humedad (%)')
    plt2.set_ylabel('Humedad (%)')
    plt2.ticklabel_format(useOffset = False)
    plt2.legend(loc = 'upper right')

while True:
    while (ser.inWaiting()==0):
        pass
    string = ser.readline().decode("utf-8")
    dataArray = string.split(',')
    te = float(dataArray[2])
    hu = float(dataArray[1])
    temp.append(te)
    humedad.append(hu)
    drawnow(makeFig)
    plt.pause(0.01)
    cnt = cnt +1
    if (cnt>50):
        temp.pop(0)
        humedad.pop(0)