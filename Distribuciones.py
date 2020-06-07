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


def getTheoryPoisson(lmda,size,quantity):
    i = 0
    arr=[]
    while i<=size:
        arr.append((mt.exp(-lmda)*lmda**i)/mt.factorial(i)*quantity)
        i+=1
    return arr


numberOfGeneratedValues = 5000 
arrAux = []
lmda = 7
i = 0
while i <=25:
    arrAux.append(i)
    i+=1
generatedPoissonValues = []
fecuencyOfPoissonValues=[0] * 26
i=0
while i<=numberOfGeneratedValues:
    generatedPoissonValues.append(getRandompoisson(lmda))
    i+=1
i=0
while i<=numberOfGeneratedValues:   
    fecuencyOfPoissonValues[generatedPoissonValues[i]]+=1
    i+=1
plt.xticks(arrAux)
plt.bar(arrAux,fecuencyOfPoissonValues)

plt.plot(arrAux,getTheoryPoisson(lmda,25,5000),color='r' ,label = "line 1")
plt.show()
print(getTheoryPoisson(lmda,25,5000))