import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random
import math


def normal(k, ex, stdx):
    sum = 0
    for i in range(k):
        r = random.uniform(0,1)
        sum = sum + r
    return ((stdx * ((12/k)**(1/2))*(sum - (k/2))) + ex)

# main 

k = 12
d = 0.2
u = 0
x = []

for i in range(1000):    
    x.append(normal(k,u,d))

mybins = np.arange(-1,1,0.02)
plt.hist(x,bins=mybins, linewidth = 0.2, weights=np.zeros_like(x) + 1./len(x), color='blue')
plt.show()

print("La media es: ","%.2f" % np.mean(x))
print("La varianza es: ","%.2f" % np.var(x))
print("La desviacion estandar es: ","%.2f" % math.sqrt(np.var(x)))


# Graficando Normal
mu, sigma = 0, 0.2 # media y desvio estandar
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

# histograma
aleatorios = normal.rvs(1000) # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Normal')
plt.show()

# prueba chi cuadrado
