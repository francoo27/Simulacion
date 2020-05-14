import scipy.stats as stat #es para sacar el valor de chi cuadrado con N grados de libertad y un alfa.
import random 
import math
import numpy as np
import matplotlib.pyplot as plt
#Generar valores con el GCL
def GenerarValoresPorGCL(z0, a, c, m):
    Ui = []
    Ui.append(z0 / m)
    zant = z0
    for i in range (999):
        zi = (zant * a + c) %m
        Ui.append(zi / m)
        zant = zi
    return Ui

#Generador de python
def llenarVectorAleatorio():
    x = []
    for i in range(1000):
        x.append(random.uniform(0,1))
    return x


# print(GenerarValoresPorGCL(4,1,2,3))
#print(math.sqrt(1000))

# Prueba de series
vector = [1,2,3,4,5]
print(vector[:-1])



