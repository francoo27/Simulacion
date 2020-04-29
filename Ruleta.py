import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


class CONSTANT:
    TIRADAS = 5000
    EUROPEA = 37
    REPETICIONES = 4
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
color = ['r', 'b', 'g', 'y', 'p']


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


# def getTableSim(players,spins):
#     tableSim = players*[spins*[0]]


def martingala(tirada, tipoApuesta, maxPer=0, minPer=0):
    capital = [100]
    apuesta = 1
    for i in tirada:
        print('Tengo:', capital[-1])
        print('Apueto: ', apuesta)

        if (capital[-1] - apuesta) < 0:
            print('No me alcanza')
            break

        if i in tipoApuesta:
            capital.append(capital[-1] + apuesta)
            apuesta = 1
            print('Gano')
        else:
            capital.append(capital[-1] - apuesta)
            apuesta = apuesta * 2
            print('Pierdo')

    # plt.suptitle('Apuestas')
    # plt.ylabel('Capital')
    # plt.xlabel('Tiradas')
    # plt.plot(capital)
    # plt.show()
    # respuesta = [[CONSTANT.TIRADAS*[0]],0]
    # respuesta[0] = capital
    # respuesta[1] = color
    return capital


# MAIN LOOP ################
tiradas = CONSTANT.REPETICIONES*[CONSTANT.TIRADAS*[0]]

fillTiradas(tiradas, CONSTANT.REPETICIONES)
# jugadas = 5*[[2*[0], '']]
# jugadas[0][1][1] = 
# jugadas[][]
# print(jugadas)


# jugadas[0][0] = martingala(tiradas[0], APUESTAS.NEGRO)
# jugadas[0][1] = 'k-o'
# jugadas[1][0] = martingala(tiradas[0], APUESTAS.ROJO)
# jugadas[1][1] = 'r-o'
# jugadas[2][0] = martingala(tiradas[0], APUESTAS.PRIMER_DOCE)
# jugadas[2][1] = 'p-o'
# jugadas[3][0] = martingala(tiradas[0], APUESTAS.SEGUNDO_DOCE)
# jugadas[3][1] = 'g-o'
# jugadas[4][0] = martingala(tiradas[0], APUESTAS.TERCER_DOCE)
# jugadas[4][1] = 'y-o'
# i = 0
# while i < CONSTANT.REPETICIONES:
#     plt.plot(jugadas[i][0],jugadas[i][1])
#     i += 1
# plt.suptitle('Apuestas')
# plt.ylabel('Capital')
# plt.xlabel('Tiradas')
# plt.show()


# 8 jugadores
# cada jugador tiene su propia tirada (aleatoria sin patrones de comportamiento por ahora)
# apuesta minima
