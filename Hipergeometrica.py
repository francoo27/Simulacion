import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import math as mt
from prettytable import PrettyTable as pt
import uuid


def hipergeometrica(p,N,n):
    x = 0
    for i in range(n): 
        r = random.random()
        if(r-p<0):
            s = 1
            x += 1
        else:
            s = 0
        p = (N*p-s)/(N-1)
        N -= 1
    return x

def getVarianza(dataset):
    esperenza = getEsperanza(dataset)
    n = len(dataset)
    acum = 0
    for i in dataset:
        acum += (i-esperenza)**2
    varianza = 1/n * acum
    return varianza

def getEsperanza(dataset):
    n = len(dataset)
    acum = 0
    for i in dataset:
        acum += i
    esperanza = acum/n
    return esperanza


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
    return arr\
    
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return mt.trunc(stepper * number) / stepper

def getMediaTeoria(p,n):
    return n*p

def getvarianzaTeoria(p,N,n):
    return  n*p*(1-p)*((N-n)/(N-1))



arr = []
i=0
while i <=1000:
    arr.append(hipergeometrica(0.5,100,10))
    i+=1
plt.xticks(getArrayFilledWithSecuencialNumbers(max(arr)))
plt.bar(getArrayFilledWithSecuencialNumbers(max(arr)),getCount(arr))
plt.show()

y = pt() 
y.title = ' Media  ,Varianza y Desviacion'
y.field_names = ["Simulacion", "Media", "Varianza", "Desviacion"]
y.add_row(["Grupo", truncate(getEsperanza(arr),7),  truncate(getVarianza(arr),7), truncate(mt.sqrt(getVarianza(arr)),7)])
y.add_row(["Teoria", getMediaTeoria(0.5,10), truncate(getvarianzaTeoria(0.5,1000,10),7), truncate(mt.sqrt(getvarianzaTeoria(0.5,1000,10)),7)])
print(y)