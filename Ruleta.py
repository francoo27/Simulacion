import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


class Constant:
    TIRADAS = 1000
    EUROPEA = 37
    REPETICIONES = 5
    INPUT = 6


colors = ['red', 'blue', 'green', 'yellow', 'purple']
color = ['r', 'b', 'g', 'y', 'p']


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
        tirada.append(random.randint(0, maxValue - 1))
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


def getFrecuenciaAbsoluta(tirada):
    frecAbs = {}
    for t in tirada:
        if t not in frecAbs.keys():
            frecAbs[t] = 1
        else:
            frecAbs[t] = frecAbs[t] + 1
    return frecAbs


def graphFrecuenciaRelativa():
    c = 0
    plt.suptitle('Frecuencia Relativa')
    while c < Constant.REPETICIONES:
        plt.plot(getFrecuenciaRelativa(tiradas[c], Constant.INPUT))
        c += 1
    plt.plot([0, Constant.TIRADAS],
             [1/Constant.EUROPEA, 1/Constant.EUROPEA], 'k-o')
    plt.annotate('Valor esperado',
                 color='black',
                 xy=(Constant.TIRADAS/2, 0.03),
                 xytext=(Constant.TIRADAS/2, 0.03)
                 )
    plt.show()


def graphValorPromedio():
    c = 0
    plt.suptitle('Valor Promedio')
    plt.plot([0, Constant.TIRADAS], [18, 18], 'k-o')
    while c < Constant.REPETICIONES:
        plt.plot(getValorPromedio(tiradas[c]))
        c += 1
    plt.annotate('Valor promedio esperado',
                 color='black',
                 xy=(Constant.TIRADAS/2, 17.95),
                 xytext=(Constant.TIRADAS/2, 19),
                 arrowprops=dict(facecolor='black',
                                 edgecolor='black',
                                 shrink=0.05),
                 )
    plt.show()


def graphVarianza():
    c = 0
    plt.suptitle('Varianza')
    while c < Constant.REPETICIONES:
        plt.plot(getVarianza(tiradas[c]))
        c += 1
    plt.show()


def graphDesviacion():
    c = 0
    plt.suptitle('Desviacion Tipica')
    while c < Constant.REPETICIONES:
        plt.plot(getDesviacion(tiradas[c]))
        c += 1
    plt.show()


def graphDesviacionRespectoMedia():
    c = 0
    plt.suptitle('Desviacion Respecto A La Media')
    while c < Constant.REPETICIONES:
        plt.plot(getDesviasionRespectoALaMedia(inputNumber, tiradas[c]))
        c += 1
    plt.show()


def graphBarrasAbsolutas():
    threshold = Constant.TIRADAS/Constant.EUROPEA
    fig, ax = plt.subplots()
    ax.plot([0, 36], [threshold, threshold], "k--")
    langs = ["Tiradas"]
    data = getFrecuenciaAbsoluta(tiradas[0])
    df = pd.DataFrame(data, index=langs).transpose()
    plt.bar(df.index, df["Tiradas"])
    plt.xticks(df.index)
    plt.suptitle('Frecuencia Absoluta')
    plt.ylabel('Cantidad de Apariciones')
    plt.xlabel('Numeros de la Ruleta')
    plt.show()


def fillTiradas(tiradas):
    c = 0
    while c < Constant.REPETICIONES:
        tiradita = getTirada(Constant.TIRADAS, Constant.EUROPEA)
        tiradas[c] = tiradita
        c += 1


# MAIN LOOP ################
tiradas = Constant.REPETICIONES*[Constant.TIRADAS*[0]]

fillTiradas(tiradas)
# print(tiradas)
# Grafica frecuencia absoluta (en barras)
graphBarrasAbsolutas()
# Grafica frecuencia relativa
graphFrecuenciaRelativa()
# Grafica valor promedio
plt.figure()
graphValorPromedio()
# Grafica varianza
plt.figure()
graphVarianza()
# Grafica desviacion
plt.figure()
graphDesviacion()
# Grafica desviasion respecto a la media
plt.figure()
# graphDesviacionRespectoMedia()
