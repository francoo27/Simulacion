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




rangos = [range(0,10),range(10,21),range(21,31),
range(31,41),range(41,51),range(51,61),
range(61,71),range(71,81),range(81,91),range(91,101)]

# FO = [0,0,0,0,0,0,0,0,0,0]
# FOA = [0,0,0,0,0,0,0,0,0,0]
# POA = [0,0,0,0,0,0,0,0,0,0]
# PEA = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
TABLA = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
[0,0,0,0,0,0,0,0,0,0]
]


numeros = [63, 14, 76, 12, 48, 46, 8, 45, 10, 68,
34,	19,	85,	7,  72,	33,	60,	97,	53,	34,
63,	50,	4,	11,	9,	79,	29,	54,	67,	78,
45,	50,	60,	66,	31,	53,	74,	84,	53,	16,
63,	71,	77,	3,	44,	7,	82,	41,	17,	62,
89,	35,	45,	74,	27,	36,	22,	75,	17,	39,
96,	88,	55,	24,	39,	14,	25,	32,	30,	23,
12,	27,	41,	39,	49,	41,	82,	23,	75,	17,
98,	93,	77,	47,	58,	69,	82,	83,	44,	25,
54,	73,	57,	90,	91,	54,	73,	95,	86,	65]
#CALCULO FO
i = 0
k = 0
for numero in numeros:
    k = 0
    for rango in rangos:
        if numero in rango:
            (TABLA[0])[k] += 1
        k += 1
    i+=1
#CALCULO FOA , POA , |PEA - POA|
i = 0
acum = 0
for frecuencia in TABLA[0]:
    acum += frecuencia 
    (TABLA[1])[i] = acum
    (TABLA[2])[i] = acum/100
    (TABLA[4])[i] = abs((TABLA[3])[i] - (TABLA[2])[i])
    i += 1
maxIndex = np.where(TABLA[4] == np.amax(TABLA[4]))
maxIndex = (maxIndex[0])[0] 
DMCrit = (1.36/100)
print(' RANGO         |  FO   |  FOA  |   POA    |  PEA  |   (|PEA - POA|)    |')
print('---------------------------------------------------------------------------')
i = 0
for c in TABLA[1]:
    if ( i == maxIndex):
        print(" %(5)s | %(0)s      | %(1)s     | %(2)s  |   %(3)s |  %(4)s  |" % {'0':  (TABLA[1])[i], '1': (TABLA[1])[i],
                                                                                    '2': (TABLA[2])[i],'3': (TABLA[3])[i],
                                                                                    '4': '\033[93m'+str((TABLA[4])[i])+'\033[0m','5':rangos[i]})
        print('---------------------------------------------------------------------------')
    else:
        print(" %(5)s | %(0)s      | %(1)s     | %(2)s  |   %(3)s |  %(4)s  |" % {'0':  (TABLA[1])[i], '1': (TABLA[1])[i],
                                                                                '2': (TABLA[2])[i],'3': (TABLA[3])[i],
                                                                                '4': (TABLA[4])[i],'5':rangos[i]})
        print('---------------------------------------------------------------------------')
    i +=1 
if(TABLA[4][maxIndex]<=DMCrit):
    print(('\033[92m'+' %(0)s SE ACEPTA HIPOTESIS'+'\033[0m')%{'0':str(TABLA[4][maxIndex]) + ' <= ' + str(DMCrit)})
else:
    print(('\033[91m'+' %(0)s SE RECHAZA HIPOTESIS'+'\033[0m') % {'0':str(TABLA[4][maxIndex]) + ' > ' + str(DMCrit)})
print('---------------------------------------------------------------------------')
# print(TABLA)
# print(maxIndex)
# print(numeros)
