"""size = 200
x = 0

for i in range(size):
    print(x)
    x += 1

print("terminado")"""

i = 0
voltaje = []
corriente = []

while i < 600:
    linea =input("Ingresa Dato: ")
    #string = linea.decode()
    sep = linea.split(",")
    voltaje.append(sep[1])
    corriente.append(sep[2])
    i += 1

print(voltaje)
print(corriente)


