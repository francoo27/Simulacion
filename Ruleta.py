import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


class CONSTANT:
    TIRADAS = 500
    EUROPEA = 37
    REPETICIONES = 2
    INPUT = 6


class NIVELECONOMICO:
    MUY_ALTO = (150000, 500000)
    ALTO = (75000, 150000)
    MEDIO = (5000, 75000)
    BAJO = (100, 5000)


class APUESTAS:
    PAR = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    IMPAR = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    NEGRO = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
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
               apuestaMax, minPer=0, maxPer=0, acotado=False):
    capital = [capitalInicial]
    apuesta = apuestaInicial
    apuestaLength = len(tipoApuesta)
    for i in tirada:
        # print('Tengo:', capital[-1])
        # print('Apueto: ', apuesta)
        # if (capital[-1] >= maxPer and maxPer != 0):
        #     return capital
        if(acotado):
            if (capital[-1] - apuesta) < 0:
                break
        if i in tipoApuesta:
            capital.append((capital[-1]-apuesta) +
                           apuesta*((CONSTANT.EUROPEA-1)/apuestaLength))
            apuesta = apuestaInicial
        else:
            apuesta = apuesta * 2
            if (apuesta > apuestaMax):
                apuesta = apuestaMax     
            capital.append(capital[-1] - apuesta)
    return capital


def getFlujoDeCaja(jugadas,apuestaInicial):
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
        pasoCaja = 0
        while j < len(jugadas):
            if(i < len(jugadas[j])):
                pasoCaja += apuestaInicial-jugadas[j][i]
            j += 1
        caja.append(pasoCaja)    
        i += 1 
    return caja


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


##### PAROLI ######

def paroli(tiradas, tipoApuesta, apuestaInicial, capitalInicial):
    apuesta = apuestaInicial
    capital = [capitalInicial]
    cont = 1
    apuestaLength = len(tipoApuesta)
    for i in tiradas:
        print('Tengo:', capital[-1])
        print('Apueto: ', apuesta)

        if (capital[-1] - apuesta) < 0:
#             print('No me alcanza')
            break

        if i in tipoApuesta:
            capital.append((capital[-1]-apuesta) +
                           apuesta*((CONSTANT.EUROPEA-1)/apuestaLength))
            cont += 1
            if cont == 4:
                cont = 1
            apuesta = apuestaInicial * cont
            print('Gano')
        else:
            capital.append(capital[-1] - apuesta)
            apuesta = apuestaInicial
            cont = 1
            print('Pierdo')
    return capital

# fibonacci(100)
# FibArray.pop(0)


def estraFib(tirada, tipoApuesta):
    capital = [100]
    c = 0
    apuesta = FibArray[c]
    apuestaLength = len(tipoApuesta)
    for i in tirada:
        print('Tengo:', capital[-1])
        print('Apueto: ', apuesta)

        # if (capital[-1] - apuesta) < 0:
        #     print('No me alcanza')
        #     break

        if i in APUESTAS.NEGRO:
            capital.append((capital[-1]-apuesta) +
                apuesta*((CONSTANT.EUROPEA-1)/apuestaLength))
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


def getFrecuenciaRelativa(tirada):
    cont = [0, 0, 0]
    c = 0
    while c < len(tirada):
        if(tirada[c] == 0):
            cont[0] += 1
        if(tirada[c] in APUESTAS.NEGRO):
            cont[1] += 1
        if(tirada[c] in APUESTAS.ROJO):
            cont[2] += 1
        c += 1
    return cont

# MAIN LOOP ################
tiradas = CONSTANT.REPETICIONES*[CONSTANT.TIRADAS*[0]]
fillTiradas(tiradas, CONSTANT.REPETICIONES)
# # jugadas = 5*[[[0]]]
jugadas = [[0]*CONSTANT.TIRADAS for i in range(CONSTANT.REPETICIONES)]
# i = 0
# contadordeceros = 0
# while i < len(tiradas[0]):
#     if (tiradas[0][i] == 0):
#         contadordeceros += 1
#         plt.axvline(x=i, ymin=0, ymax=15000, linestyle='dashed')
#     i += 1
# print(contadordeceros)
capitalInicial = 100
apuestaInicial = 5
jugadas[0] = martingala(tiradas[0], APUESTAS.NEGRO, 5, apuestaInicial,50,True)
jugadas[1] = martingala(tiradas[0], APUESTAS.NEGRO, 5, apuestaInicial,50)
plt.plot(jugadas[0], color[0])
plt.plot(jugadas[1], color[1])
# plt.plot(paroli([2,2,1,2,1], APUESTAS.NEGRO,apuestaInicial,capitalInicial), '-o')
# plt.plot(paroli([1,2,2,2,1], APUESTAS.NEGRO,apuestaInicial,capitalInicial), '-o')
# plt.plot(paroli([2,2,2,2,2], APUESTAS.NEGRO,apuestaInicial,capitalInicial), '-o')
plt.show()
# jugadas[0] = martingala(tiradas[0], APUESTAS.NEGRO, 5, apuestaInicial,50)
# jugadas[1] = martingala(tiradas[0], APUESTAS.ROJO, 5, apuestaInicial,50)
# jugadas[2] = martingala(tiradas[0], APUESTAS.PRIMER_DOCE, 25, apuestaInicial,50)
# jugadas[3] = martingala(tiradas[0], APUESTAS.SEGUNDO_DOCE, 25, apuestaInicial,50)
# jugadas[4] = martingala(tiradas[0], APUESTAS.TERCER_DOCE, 25, apuestaInicial,50)
# # print(jugadas)
# i = 0
# while i < CONSTANT.REPETICIONES:
#     plt.plot(jugadas[i], color[i])
#     i += 1
# plt.plot(getFlujoDeCaja(jugadas,apuestaInicial),'g-')
# # plt.plot(estraFib(tiradas[0]))
# plt.suptitle('Apuestas')
# plt.ylabel('Capital')
# plt.xlabel('Tiradas')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid(True, which='both')
# plt.show()
# print(getFrecuenciaRelativa(tiradas[0])[0])
# print(getFrecuenciaRelativa(tiradas[0])[1])
# print(getFrecuenciaRelativa(tiradas[0])[2])


# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(getFrecuenciaRelativa(tiradas[0]), colors=['green', 'black', 'red'],
#         autopct='%1.1f%%', textprops={'color': "w"},
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax1.legend(['Cero', 'Negro', 'Rojo'], loc="upper right")
# plt.show()
# plt.plot(paroli(tiradas[0], APUESTAS.NEGRO), '-o')
# plt.suptitle('Apuestas')
# plt.ylabel('Capital')
# plt.xlabel('Tiradas')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid(True, which='both')
# plt.show()
