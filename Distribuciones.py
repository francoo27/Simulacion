import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import math as mt
from prettytable import PrettyTable as pt
import uuid

# HIPERGEOMÉTRICA 
# POISSON 
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

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return mt.trunc(stepper * number) / stepper

def testChiCuadrado(frecuencies,expectedFrecuencies):
    i=x=0
    ## se va testear con un valor fijo de 1 grado de libertad y un nivel de significacia de 0.005 = 7.879
    testVal = 7.879
    for e in frecuencies:
        x += ((e - expectedFrecuencies[i] )** 2) / expectedFrecuencies[i]
        i+=1
    return([x,x < testVal])

def most_frequent(arr): 
    return np.bincount(arr).argmax()




simulationUUID = uuid.uuid4()
numberOfGeneratedValues = 5000 
lmda = 7

# Valores teoricos de distribucion de poisson
teoryPoisson = getTheoryPoisson(lmda,25,5000)
#Grafico de frecuencia generada por el equipo
teamPoisson = getRandompoissonArray(lmda,numberOfGeneratedValues)
#Grafico de frecuencia generada por libreria
libPoisson = np.random.poisson(lam=lmda, size=numberOfGeneratedValues)

#Grafico de frecuencia teorica
plt.plot(getArrayFilledWithSecuencialNumbers(len(teoryPoisson)-1),teoryPoisson,'r-o')
#Grafico de frecuencia del equipo
teamFrecuencyPoisson = getFrecuency(teamPoisson)
plt.plot(getArrayFilledWithSecuencialNumbers(len(getFrecuency(teamPoisson))-1),teamFrecuencyPoisson,'g-o')
# # plt.xticks(getArrayFilledWithSecuencialNumbers(max(libPoisson)))
# # plt.bar(getArrayFilledWithSecuencialNumbers(max(libPoisson)),getCount(libPoisson))
plt.show()


#Grafico de frecuencia teorica
plt.plot(getArrayFilledWithSecuencialNumbers(len(teoryPoisson)-1),teoryPoisson,'r-o')
#Grafico de frecuencia de la libreria
libFrecuencyPoisson=getFrecuency(libPoisson)
plt.plot(getArrayFilledWithSecuencialNumbers(max(libPoisson)),libFrecuencyPoisson,'b-o')
plt.show()



f= open("Distribuciones" + str(simulationUUID) + ".txt","w+")
x = pt()
x.title = 'Resultados de simulacion utilizando valores generados por el equipo'
x.field_names = ["Numero", "Frecuencia obtenida", "Probabilidad esperada", "Variacion con respecto a teorica"]
i=0
for e in teamFrecuencyPoisson:
    x.add_row([i,truncate(e,7),truncate(teoryPoisson[i],7),truncate(e - teoryPoisson[i],7) ])
    i+=1
print(x)
f.write(x.get_string())
testChi = testChiCuadrado(libFrecuencyPoisson,teoryPoisson)
if(testChi[1]):
    f.write("Paso Test de chi cuadrado")
    print("Paso Test de chi cuadrado")
else:
    print("No paso Test de chi cuadrado")
    f.write("No Paso Test de chi cuadrado")   
x = pt()
x.title = 'Resultados de simulacion utilizando la libreria de python'
x.field_names = ["Numero", "Frecuencia obtenida", "Probabilidad esperada", "Variacion con respecto a teorica"]
i=0
for e in libFrecuencyPoisson:
    x.add_row([i,truncate(e,7),truncate(teoryPoisson[i],7),truncate(e - teoryPoisson[i],7) ])
    i+=1
print(x)
f.write(x.get_string())
testChi = testChiCuadrado(libFrecuencyPoisson,teoryPoisson)
if(testChi[1]):
    print("Paso Test de chi cuadrado")
    f.write("Paso Test de chi cuadrado")
else:
    print("No paso Test de chi cuadrado")
    f.write("No Paso Test de chi cuadrado") 


y = pt() 
y.title = ' Media ,Varianza y Desviacion'
y.field_names = ["Simulacion", "Media","Moda", "Varianza", "Desviacion"]
y.add_row(["Grupo", truncate(np.mean(teamPoisson),7),most_frequent(teamPoisson), truncate(np.var(teamPoisson),7), truncate(np.std(teamPoisson),7)])
y.add_row(["Python", truncate(np.mean(libPoisson),7),most_frequent(libPoisson), truncate(np.var(libPoisson),7), truncate(np.std(libPoisson),7)])
y.add_row(["Teoria", lmda, lmda-1, lmda, truncate(mt.sqrt(lmda),7)])
print(y)
f.write(y.get_string())

f.close()