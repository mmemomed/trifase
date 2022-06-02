#Obtención de datos de un motor trifásico

import serial, serial.tools.list_ports #Library to identify the ports
import time 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    ser = serial.Serial(conPuerto, baudrate = 9600, timeout = 0)

    print('Conectado al puerto: ' + conPuerto)
else:
    print('Error de Conexión')

#RECOGE LOS DATOS Y LOS ALMACENA EN UNA lISTA
#voltajex = []
#corrientex = []

#voltajey = []
#corrientey = []

#voltajez = []
#corrientez = []

temperatura = [] #lista para almacenar los datos de voltaje
humedad = [] #Lista para almacenar los datos de corriente
tiempo = []
tiempo2 = []

'''def graf1(i):
    sep = string.split(',')
    h1 = float(sep[1])
    c1 = float(sep[2])
    t1 = int(sep[0])
    tiempo.append(t1)
    humedad.append(h1)
    temperatura.append(c1)
    plt.cla()
    plt.plot(tiempo,humedad)
    plt.plot(tiempo, temperatura)
    plt.xlabel("Tiempo")
    plt.xlabel("Temperatura/Humedad")
    plt.tight_layout()'''


while True:    
    puertosEnc = obtpuerto()
    conPuerto = encArduino(puertosEnc)
    if conPuerto == 'None':     #ROMPE EL CICLO SI SE DESCONECTA EL ARDUINO
        break
    linea = ser.readline()
    string = linea.decode()
    if string != '':
        sep = string.split(',')
        pvar = float(sep[0])
        svar = float(sep[1])
        tvar = float(sep[2])
        tiempo.append(pvar)
        tiempo2.append(pvar)
        humedad.append(svar)
        temperatura.append(tvar)

    print()
    time.sleep(1)


'''
while True:
    data = ser.readline()
    string = data.decode()
    if string != '':
        sep = string.split(',')
        pvar = float(sep[0])
        svar = float(sep[1])
        tvar = float(sep[2])
        tiempo.append(pvar)
        tiempo2.append(pvar)
        humedad.append(svar)
        temperatura.append(tvar)
        plt.scatter(tiempo, humedad)
        plt.show()
        plt.pause(1)'''





    


    
#anim1 = FuncAnimation(plt.gcf(), graf1, interval = 1000)
#plt.show()


    



'''
for i in range(size):
    linea = ser.readline() #Lectura de líneas de datos
    string = linea.decode() #Transformar los datos a string
    sep = string.split(",") 
    voltaje.append(sep[1]) #Obtener el voltaje de esta línea
    corriente.append(sep[2]) #Obtener la corriente de esta línea
'''