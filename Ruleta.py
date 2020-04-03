import matplotlib.pyplot as plt 
import numpy as np
import random

def RealizarTirada():
    return random.randint(0,36)

lista = []

#Frecuencia relativa de un numero X(6) con resoecto a N
frecRelativa6 = []
cantDe6 = 0

#Valor promedio de las tiradas con respecto a N
valorPromedio = []
promedio = 0

#Valor del desvio del .... ???

#Valor de la varianza del numero X(6) con respecto a N
#varianza6 = []



for i in range(1,500000):
    #Resultado de las tiradas
    tirada = RealizarTirada()
    lista.append(tirada)

    #Valor promedio   
    #valorPromedio.append(np.mean(lista)) #con mean toma demasiado tiempo
    promedio = promedio + tirada
    valorPromedio.append(promedio/i)

    #Frecuencia relativa
    if tirada == 6 :
        cantDe6 = cantDe6 + 1 
    frecRelativa6.append(cantDe6/i)

#Grafica frecuencia relativa
#plt.plot(frecRelativa6)
#plt.show

#Grafica valor promedio
plt.plot(valorPromedio)
plt.show()

#Lista completa de tiradas
#for i in (lista):
#    print (lista[i])