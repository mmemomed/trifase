#Obtención de datos de un motor trifásico

import serial, serial.tools.list_ports #Library to identify the ports
import time

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
temperatura = [] #lista para almacenar los datos de voltaje
humedad = [] #Lista para almacenar los datos de corriente

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
        humedad.append(pvar)
        temperatura.append(svar)
        #print(pvar)
        #print(svar)

    time.sleep(1)

print('Terminado')
print(temperatura)
print(humedad)



'''
for i in range(size):
    linea = ser.readline() #Lectura de líneas de datos
    string = linea.decode() #Transformar los datos a string
    sep = string.split(",") 
    voltaje.append(sep[1]) #Obtener el voltaje de esta línea
    corriente.append(sep[2]) #Obtener la corriente de esta línea
'''



