import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random
import math


def pascal(k,q):
    tr = 1
    qr = math.log(q)
    for i in range(k):
        r = random.uniform(0,1)
        tr = tr * r
    nx = (math.log(tr)) / qr  
    return nx

# main 
k = 5
q = 0.5
x = []

for i in range(10000):    
    x.append(pascal(k,q))


mybins = np.arange(0,25,1)
plt.hist(x,bins=mybins, linewidth = 0.2, weights=np.zeros_like(x) + 1./len(x), color='blue')
plt.show()


def pascal1(k,q):

    sum = 0
    for i in range(k):
        r = random.random()
        sum += math.log(r)

    x = sum/ math.log(q)
    return x

for i in range(10000):    
    x.append(pascal1(k,q))

mybins = np.arange(0,25,1)
plt.hist(x,bins=mybins, linewidth = 0.2, weights=np.zeros_like(x) + 1./len(x), color='blue')
plt.show()

