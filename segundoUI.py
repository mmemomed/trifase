import serial 
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def getSerialData(self,Samples,serialConnection,lines,lineValueText,lineLabel):
    value = float(serialConnection.readline().strip()) #Leer sensor
    data.append(value) #Guarda lectura en la última posición
    lines.set_data(range(Samples,data)) #Dibujar nueva línea
    lineValueText.set_text(lineLabel+' = '+str(round(value,2))) #Mostrar valor del sensor

#Copiar funciones para hacer la conección

Samples = 100 #Muestras
data = collections.deque([0]*Samples,maxlen=Samples) #Vector de muestras
sampleTime = 100  #Tiempo de muestreo

#Límites de los ejes
xmin = 0
xmax = Samples
ymin = 0
ymax = 6

fig = plt.figure(figsize = (13,6)) #Crae una nueva figura 
ax = plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax)) #Establece los límites 
plt.title("Real-time Sensor reading")