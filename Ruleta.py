import matplotlib.pyplot as plt
import numpy as np
import random


class Constant:
    TIRADAS = 10000
    CANTMONTECARLO = 36


colors = ['red', 'blue', 'green', 'yellow', 'purple']
color = ['r', 'b', 'g', 'y', 'p']


def getInput():
    correct = False
    while correct != True:
        inputNumber = int(input("Dígame un número de la ruleta (entre 0 y 36):"))
        if inputNumber >= 0 and inputNumber <= Constant.CANTMONTECARLO:
            correct = True
        else:
            print('Numero Fuera de indice, Elija entre 0 y 36')
    else:
        return inputNumber


def getValorPromedio(tirada):
    c = 0
    promedio = 0
    valorPromedio = []
    for i in tirada:
        c += 1
        promedio = promedio + i
        valorPromedio.append(promedio/c)
    return valorPromedio


def getFrecuenciaRelativa(tirada, input):
    frecRelativaNum = []
    absoluteFrecuency = 0
    c = 0
    for i in tirada:
        c = c + 1
        if i == input:
            absoluteFrecuency = absoluteFrecuency + 1
        frecRelativaNum.append(absoluteFrecuency/c)
    return frecRelativaNum


def getTirada(quantity, maxValue):
    tirada = []
    for i in range(1, quantity):
        # Obtener valor random dentro de el rango y añadirlo a la lista
        tirada.append(random.randint(0, maxValue))
    return tirada


def getVarianza(tirada):
    varianzaArr = []
    c = 1
    tiradaLenght = len(tirada)
    while c < tiradaLenght:
        varianzaArr.append(np.var(tirada[0:c]))
        c += 1
    return varianzaArr


def getDesviacion(tirada):
    return np.sqrt(getVarianza(tirada))


def getDesviasionRespectoALaMedia(input, tirada):
    c = 0
    promedio = 0
    DesvRespMedia = []
    for i in tirada:
        c += 1
        promedio = promedio + i
        media = promedio/c
        DesvRespMedia.append(input-media)
    return DesvRespMedia

################ MAIN LOOP ################
inputNumber = getInput()
tirada = getTirada(Constant.TIRADAS, Constant.CANTMONTECARLO)

# Grafica frecuencia relativa
# plt.plot(getFrecuenciaRelativa(tirada, inputNumber))
# plt.show()

# Grafica valor promedio
# plt.figure()
# plt.plot([-100, Constant.TIRADAS], [18, 18], 'r-o')
# plt.plot(getValorPromedio(tirada))
# plt.annotate('Valor promedio esperado',color='red', xy=(Constant.TIRADAS/2, 17.95), xytext=(Constant.TIRADAS/2, 19),
#              arrowprops=dict(facecolor='red', edgecolor='red', shrink=0.05),
#              )
# plt.show()

# Grafica varianza
# plt.figure()
# plt.plot(getVarianza(tirada))
# plt.show()


# Grafica desviacion
# plt.figure()
# plt.plot(getDesviacion(tirada))
# plt.show()

# Grafica desviasion respecto a la media
plt.figure()
plt.plot((inputNumber, tirada))
plt.show()


# Lista completa de tiradas
# for i in (lista):
#    print (lista[i])

# plt.suptitle('%i Tiradas' % n)
# plt.ylabel('S (desvio)')
# plt.xlabel('n (Numero de tiradas)')
