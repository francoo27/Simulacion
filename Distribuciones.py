import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import math as mt


# HIPERGEOMÉTRICA 
# POISSON 
# def poisson(p,x):
# #     x = 0
# #     b = mt.exp(-p)
# #     tr = 1.0
# #     r = random.random()
# #     tr = tr * r
# #     if (tr < b):
# #         x = x + 1.0
# #     else: 
## asi copie la de el libro y no entendi
## nose porque le paso x si dsp la pongo en 0
def getRandompoisson(lmda):
    x = 0
    tr = 1
    accepted = False
    while (accepted != True): 
        r = random.random()
        tr = tr * r
        if (tr < mt.exp(-lmda)):
            accepted = True
        else:
            x = x + 1
    return x
def getRandompoissonArray(lmda,numberOfGeneratedValues):
    arr = [0] * ( numberOfGeneratedValues )
    i = 0
    while i<numberOfGeneratedValues:
        arr[i] = getRandompoisson(lmda)
        i+=1
    return arr



def getTheoryPoisson(lmda,size,quantity):
    i = 0
    arr=[]
    while i<=size:
        arr.append((mt.exp(-lmda)*lmda**i)/mt.factorial(i))
        i+=1
    return arr

def getFrecuency(arr):
    arr.sort()
    frecuencyCounter = [0] * ( arr[-1] + 1 )
    sizeOfArr = len(arr)
    for e in arr:
        frecuencyCounter[e] += 1/sizeOfArr
    # print(arr)
    # print(maxNumber)
    # print(frecuencyCounter)
    return frecuencyCounter

def getCount(arr):
    arr.sort()
    counter = [0] * ( arr[-1] + 1 )
    for e in arr:
        counter[e] += 1
    return counter

def getArrayFilledWithSecuencialNumbers(maxValue):
    arr= [0] * ( maxValue + 1 )
    i = 0
    while i <= maxValue:
        arr[i] = i
        i+=1
    return arr

def getArrayFilledWithZeroes(size):
    arr= [0] * ( size ) 
    return arr


numberOfGeneratedValues = 5000 
arrAux = []
lmda = 7
#Grafico de frecuencia generada por el equipo
arr = getRandompoissonArray(lmda,numberOfGeneratedValues)
# print(getRandompoissonArray(lmda,numberOfGeneratedValues))
# plt.xticks(arrAux)
# plt.bar(getArrayFilledWithSecuencialNumbers(max(arr)),getCount(arr))
plt.plot(getArrayFilledWithSecuencialNumbers(len(getFrecuency(arr))-1),getFrecuency(arr),color='g')


libPoisson = np.random.poisson(lam=lmda, size=5000)
# plt.xticks(getArrayFilledWithSecuencialNumbers(max(libPoisson)))
# plt.bar(getArrayFilledWithSecuencialNumbers(max(libPoisson)),getCount(libPoisson))
#Grafico de frecuencia teorica
teoryPoisson = getTheoryPoisson(lmda,25,5000)
plt.plot(getArrayFilledWithSecuencialNumbers(len(teoryPoisson)-1),teoryPoisson,color='r')
#Grafico de frecuencia generada por libreria
plt.plot(getArrayFilledWithSecuencialNumbers(max(libPoisson)),getFrecuency(libPoisson))
plt.show()


