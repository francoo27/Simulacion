import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random
import math

def binom(n,p):
    x = 0
    for i in range(n):
        r = random.uniform(0,1)
        if (r <= p):
            x = x + 1 
    return x

# main 
n, p = 50, 0.3
x = []

for i in range(1000):    
    x.append(binom(n,p))

mylabel = "n={}, p={}".format(n,p)
plt.hist(x, bins=np.arange(0,n,1), color='tomato', linewidth=1, edgecolor = 'red', alpha = 0.5, label=mylabel, weights=np.zeros_like(x) + 1. /len(x))
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.savefig('Binomial generada')
plt.show()

ex = n*p 
print("La esperanza es: ",ex)
q = (1-p)
vx = n*p*q
print("La varianza es: ",vx)

# Forma directa
# def numero_combinaciones(m,n):
#     if m < n:
#         return 0
#     else:
#         comb = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
#         return comb

# def binomDirecta(n):
#     x = []
#     for i in range(n):
#         comb = numero_combinaciones(n,i)
#         px = p**i
#         qnx = q**(n-i)
#         fx = comb*px*qnx
#         x.append(fx)
#     return x

# x = []
# x = binomDirecta(n)
# plt.plot(np.arange(0,n,1), x)
# plt.show()
    

# Por libreria de Python
# Graficando Binomial
n, p = 50, 0.3 # parametros de forma 
binomial = stats.binom(n, p) # Distribución
x = np.arange(binomial.ppf(0.01), binomial.ppf(0.99))
x = np.arange(0,n,1)
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial por pascal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.savefig('Binomial pascal')
plt.show()

print('Media:', np.mean(x))
print('Varianza:', np.var(x))