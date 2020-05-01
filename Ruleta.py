import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


class CONSTANT:
    TIRADAS = 5000
    EUROPEA = 37
    REPETICIONES = 5
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
    DIECIOCHO_A_TREINTISEIS = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


colors = ['red', 'blue', 'green', 'yellow', 'purple']
color = ['r', 'k', 'g', 'y', 'b']


def getTirada(quantity, maxValue):
    tirada = []
    for i in range(1, quantity):
        # Obtener valor random dentro de el rango y añadirlo a la lista
        tirada.append(random.randint(0, maxValue - 1))
    return tirada


def fillTiradas(tiradas, repeticiones):
    c = 0
    while c < repeticiones:
        tiradita = getTirada(CONSTANT.TIRADAS, CONSTANT.EUROPEA)
        tiradas[c] = tiradita
        c += 1


def martingala(tirada, tipoApuesta, apuestaInicial, capitalInicial,
               maxPer=0, minPer=0):
    capital = [capitalInicial]
    apuesta = apuestaInicial
    apuestaLength = len(tipoApuesta)
    for i in tirada:
        print('Tengo:', capital[-1])
        print('Apueto: ', apuesta)
        if (capital[-1] >= maxPer and maxPer != 0):
            return capital

        if (capital[-1] - apuesta) < 0:
            break
        if i in tipoApuesta:
            capital.append((capital[-1]-apuesta) +
                           apuesta*((CONSTANT.EUROPEA-1)/apuestaLength))
            apuesta = apuestaInicial
        else:
            capital.append(capital[-1] - apuesta)
            apuesta = apuesta * 2
    return capital


def getFlujoDeCaja(jugadas):
    i = 0
    j = 0
    k = 0
    maxlen = 0
    caja = []
    while k < len(jugadas):
        if len(jugadas[k]) > maxlen:
            maxlen = len(jugadas[k])
        k += 1
    while i < maxlen:
        j = 0
        while j < len(jugadas):
            pasoCaja = 0
            if(i < len(jugadas[j])):
                # print(jugadas[j][i])
                pasoCaja += 100-jugadas[j][i]
            j += 1
            caja.append(pasoCaja)
        i += 1
    # print(caja)


# MAIN LOOP ################
# tiradas = CONSTANT.REPETICIONES*[CONSTANT.TIRADAS*[0]]

# fillTiradas(tiradas, CONSTANT.REPETICIONES)
# jugadas = 5*[[[0]]]
# jugadas = [[0]*CONSTANT.TIRADAS for i in range(CONSTANT.REPETICIONES)]


# jugadas[0] = martingala(tiradas[0], APUESTAS.NEGRO, maxPer=200)
# # jugadas[0][1] = 'k-o'
# jugadas[1] = martingala(tiradas[0], APUESTAS.ROJO)
# # jugadas[1][1] = 'r-o'
# jugadas[2] = martingala(tiradas[0], APUESTAS.PRIMER_DOCE)
# jugadas[3] = martingala(tiradas[0], APUESTAS.SEGUNDO_DOCE)
# jugadas[4] = martingala(tiradas[0], APUESTAS.TERCER_DOCE)
# i = 0
# while i < CONSTANT.REPETICIONES:
#     print(i)
#     plt.plot(jugadas[i], color[i])
#     i += 1
# plt.suptitle('Apuestas')
# plt.ylabel('Capital')
# plt.xlabel('Tiradas')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid(True, which='both')
# plt.show()

# 8 jugadores
# cada jugador tiene su propia tirada (aleatoria sin patrones de comportamiento por ahora)
# apuesta minima

FibArray = [0, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib

fibonacci(100)
FibArray.pop(0)


def estraFib(tirada):
    capital = [100]
    c = 0
    apuesta = FibArray[c]
    for i in tirada:
        print('Tengo:', capital[-1])
        print('Apueto: ', apuesta)

        if (capital[-1] - apuesta) < 0:
            # print('No me alcanza')
            break

        if i in APUESTAS.NEGRO:
            capital.append(capital[-1] + apuesta)
            c = c - 2
            if c < 0:
                c = 0
            apuesta = FibArray[c]
            # print('Gano')
        else:
            capital.append(capital[-1] - apuesta)
            c += 1   
            apuesta = FibArray[c]
            # print('Pierdo')
    return capital

# MAIN LOOP ################
tiradas = CONSTANT.REPETICIONES*[CONSTANT.TIRADAS*[0]]
fillTiradas(tiradas, CONSTANT.REPETICIONES)
jugadas = 5*[[[0]]]
jugadas = [[0]*CONSTANT.TIRADAS for i in range(CONSTANT.REPETICIONES)]
i = 0
contadordeceros=0
while i < len(tiradas[0]):
    if (tiradas[0][i] == 0):
        contadordeceros+=1
        plt.axvline(x=i, ymin=0, ymax=15000, linestyle='dashed')
    i += 1
print(contadordeceros)
jugadas[0] = martingala(tiradas[0], APUESTAS.NEGRO, 1, 100)
jugadas[1] = martingala(tiradas[0], APUESTAS.ROJO, 1, 100)
jugadas[2] = martingala(tiradas[0], APUESTAS.PRIMER_DOCE, 1, 100)
jugadas[3] = martingala(tiradas[0], APUESTAS.SEGUNDO_DOCE, 1, 100)
jugadas[4] = martingala(tiradas[0], APUESTAS.TERCER_DOCE, 1, 100)
# getFlujoDeCaja(jugadas)
print(jugadas)
i = 0
while i < CONSTANT.REPETICIONES:
    plt.plot(jugadas[i], color[i])
    i += 1
plt.plot(estraFib(tiradas[0]))
plt.suptitle('Apuestas')
plt.ylabel('Capital')
plt.xlabel('Tiradas')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True, which='both')
plt.show()


