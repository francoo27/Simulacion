import random
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
fa = [0.1,0.2,0.4,0.6,0.7,0.8,
        0.85,0.9,0.95,1]


def getFrecuency(arr):
    arr.sort()
    frecuencyCounter = [0] * ( arr[-1] + 1 )
    sizeOfArr = len(arr)
    for e in arr:
        frecuencyCounter[e] += 1/sizeOfArr
    return frecuencyCounter

def getFrecuencyAcum(arr):
    arr=getFrecuency(arr)
    frecuencyCounter = [0] * (len(arr))
    i=0
    while i < len(arr):
        k=0      
        while k<=i:
            frecuencyCounter[i] += arr[k]
            print(arr[k])
            k+=1
        i+=1
    return frecuencyCounter

arreglo = []

for i in range(10):
    arreglo.append(1)
    arreglo.append(2)
    arreglo.append(6)
    arreglo.append(5)

for i in range(20):
    arreglo.append(3)
    arreglo.append(4)

for i in range(5):
    arreglo.append(7)
    arreglo.append(8)
    arreglo.append(9)
    arreglo.append(10)

valores = []
for i in range(1000):
    r = random.uniform(0,1)
    c = 0
    b = True
    while (b):
        if (r<=fa[c]):
            valores.append(x[c])
            b = False
        else:
            c += 1

plt.hist(valores,bins=len(valores),
edgecolor ='blue',linewidth = 7,
color = 'blue',
weights=np.zeros_like(valores)+1)
frecuenciasValores= getFrecuencyAcum(valores)
i=0
while i <10:
    plt.plot([i,i+1],[frecuenciasValores[i]*1000,frecuenciasValores[i]*1000], 'k-')
    plt.plot([i,i+1], [fa[i]*1000,fa[i]*1000], 'r-')
    i+=1
plt.show()
