import random
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
fa = [0.1,0.2,0.4,0.6,0.7,0.8,
        0.85,0.9,0.95,1]
fr = [0.1,0.1,0.2,0.2,0.1,0.1,
        0.05,0.05,0.05,0.05]


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
            k+=1
        i+=1
    return frecuencyCounter
def adjustFrecuency(fa,n):
    i=0
    while i<len(fa):
        fa[i]=fa[i]*n
        i+=1
    return fa

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
adjustedFrecuency = adjustFrecuency(fr,1000)
plt.bar([1,2,3,4,5,6,7,8,9,10],adjustedFrecuency,color ='red')
plt.hist(valores,bins=len(valores),
edgecolor ='blue',linewidth = 15,
color = 'blue',
weights=np.zeros_like(valores)+1)
frecuenciasValores= getFrecuencyAcum(valores)
plt.show()
plt.step([1,2,3,4,5,6,7,8,9,10], fa)
plt.step([0,1,2,3,4,5,6,7,8,9,10], frecuenciasValores)
plt.show()