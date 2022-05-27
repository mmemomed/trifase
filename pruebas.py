"""size = 200
x = 0

for i in range(size):
    print(x)
    x += 1

print("terminado")"""

size = 10
voltaje = []
corriente = []

for i in range(size):
    linea =input("Ingresa Dato: ")
    #string = linea.decode()
    sep = linea.split(",")
    voltaje.append(sep[1])
    corriente.append(sep[2])

print(voltaje)
print(corriente)


