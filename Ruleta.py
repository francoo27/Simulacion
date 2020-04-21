import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


class CONSTANT:
    TIRADAS = 120
    EUROPEA = 37
    REPETICIONES = 9
    INPUT = 6


class NIVELECONOMICO:
    MUY_ALTO = (150000, 500000)
    ALTO = (75000, 150000)
    MEDIO = (5000, 75000)
    BAJO = (100, 5000)


class APUESTAS:
    PAR = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    IMPAR = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    NEGRO = [2, 6, 4, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    ROJO = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    PRIMER_DOCE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    SEGUNDO_DOCE = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    TERCER_DOCE = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    PRIMER_COLUMNA = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    SEGUNDA_COLUMNA = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    TERCERA_COLUMNA = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    UNO_A_DIECIOCHO = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18]
    DIECIOCHO_A_TREINTISEIS = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36]


class Jugador:
    id
    numElegidos
    estiloJuego
    nivelEconomico


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
    plt.ylabel('Frecuencia Relativa')
    plt.xlabel('Cantidad de tiradas')
    while c < CONSTANT.REPETICIONES:
        plt.plot(getFrecuenciaRelativa(tiradas[c], CONSTANT.INPUT))
        c += 1
    plt.plot([0, CONSTANT.TIRADAS],
             [1/CONSTANT.EUROPEA, 1/CONSTANT.EUROPEA], 'k-o')
    plt.show()


def graphValorPromedio():
    c = 0
    plt.suptitle('Valor Promedio')
    plt.ylabel('Valor Promedio')
    plt.xlabel('Cantidad de tiradas')
    plt.plot([0, CONSTANT.TIRADAS], [18, 18], 'k-o')
    while c < CONSTANT.REPETICIONES:
        plt.plot(getValorPromedio(tiradas[c]))
        c += 1
    plt.show()


def graphVarianza():
    c = 0
    plt.suptitle('Varianza')
    plt.ylabel('Varianza')
    plt.xlabel('Cantidad de tiradas')
    plt.plot([0, CONSTANT.TIRADAS], [114, 114], 'k-o')
    while c < CONSTANT.REPETICIONES:
        plt.plot(getVarianza(tiradas[c]))
        c += 1
    plt.show()


def graphDesviacion():
    c = 0
    plt.suptitle('Desviacion Tipica')
    plt.ylabel('Desviacion Tipica')
    plt.xlabel('Cantidad de tiradas')
    plt.plot([0, CONSTANT.TIRADAS], [np.sqrt(114), np.sqrt(114)], 'k-o')
    while c < CONSTANT.REPETICIONES:
        plt.plot(getDesviacion(tiradas[c]))
        c += 1
    plt.show()


def graphDesviacionRespectoMedia():
    c = 0
    plt.suptitle('Desviacion Respecto A La Media')
    plt.ylabel('Desviacion Respecto A La Media')
    plt.xlabel('Cantidad de tiradas')
    plt.plot([0, CONSTANT.TIRADAS], [CONSTANT.INPUT - 18, CONSTANT.INPUT - 18],
             'k-o')
    while c < CONSTANT.REPETICIONES:
        plt.plot(getDesviasionRespectoALaMedia(CONSTANT.INPUT, tiradas[c]))
        c += 1
    plt.show()


def graphBarrasAbsolutas():
    threshold = CONSTANT.TIRADAS/CONSTANT.EUROPEA
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


def fillTiradas(tiradas, repeticiones):
    c = 0
    while c < repeticiones:
        tiradita = getTirada(CONSTANT.TIRADAS, CONSTANT.EUROPEA)
        tiradas[c] = tiradita
        c += 1


def getTableSim(players,spins):
    tableSim = players*[spins*[0]]


# MAIN LOOP ################
tiradas = CONSTANT.REPETICIONES*[CONSTANT.TIRADAS*[0]]

fillTiradas(tiradas, CONSTANT.REPETICIONES)
c = 0
while c < CONSTANT.REPETICIONES:
    print(tiradas[c])
    c += 1
NIVELECONOMICO.ALTO.

# 8 jugadores
# cada jugador tiene su propia tirada (aleatoria sin patrones de comportamiento por ahora)
# apuesta minima























# # Grafica frecuencia absoluta (en barras)
# graphBarrasAbsolutas()
# # Grafica frecuencia relativa
# plt.figure()
# graphFrecuenciaRelativa()
# # Grafica valor promedio
# plt.figure()
# graphValorPromedio()
# # Grafica varianza
# plt.figure()
# graphVarianza()
# # Grafica desviacion
# plt.figure()
# graphDesviacion()
# # Grafica desviasion respecto a la media
# plt.figure()
# graphDesviacionRespectoMedia()
# CONSTANT.REPETICIONES = 1
# # Grafica frecuencia absoluta (en barras)
# plt.figure()
# graphBarrasAbsolutas()
# # Grafica frecuencia relativa
# plt.figure()
# graphFrecuenciaRelativa()
# # Grafica valor promedio
# plt.figure()
# graphValorPromedio()
# # Grafica varianza
# plt.figure()
# graphVarianza()
# # Grafica desviacion
# plt.figure()
# graphDesviacion()
# # Grafica desviasion respecto a la media
# plt.figure()
# graphDesviacionRespectoMedia()
