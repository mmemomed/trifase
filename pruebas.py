"""size = 200
x = 0

for i in range(size):
    print(x)
    x += 1

print("terminado")"""

"""
i = 0
voltaje = []
corriente = []

while i < 10:
    linea =input("Ingresa Dato: ")
    #string = linea.decode()
    sep = linea.split(",")
    voltaje.append(sep[1])
    corriente.append(sep[2])
    i += 1

print(voltaje)
print(corriente)
"""
'''
import serial, serial.tools.list_ports #Library to identify the ports
import time

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

if conPuerto != "None": #Una vez encontrado el arduino nos imprimira en que puerto esta conectado
    ser = serial.Serial(conPuerto, baudrate = 115200, timeout = 0.2)

    print('Conectado al puerto: ' + conPuerto)
else:
    print('Error de Conexión')


linea = ser.readline()
string = linea.decode()
print(string)
#sep = string.split(',')


x=0



#Este ciclo while realiza la tarea asignada mientras el arduino esté conectado a la computadora
while True:
    print(x)
    x += 1
    time.sleep(1)
    puertosEnc = obtpuerto()
    conPuerto = encArduino(puertosEnc)
    if conPuerto == 'None':
        break

print("Desconectado")



humedad = []
temperatura = []

num = input("Ingrese datos: ")
ser = str(num)
sep = ser.split(',')
pvar = float(sep[1])
svar = float(sep[2])
humedad.append(pvar)
temperatura.append(svar)


print(temperatura)
print(humedad)
'''

import matplotlib.pyplot as plt
import numpy as np



datos = []
plt.axis([0,10,0,1])



for i in range(10):
    y = np.random.random()
    plt.scatter(i,y)
    plt.pause(0.5)

plt.show()






    