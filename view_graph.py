import numpy as np
import matplotlib.pyplot as plt

f = open('graph.txt','r')

data = f.read().split('\n')

datax = []
datay = []

for i in range(len(data)-1):
    tmp = data[i].split(' ')
    datax.append(int(tmp[0]))
    datay.append(int(tmp[1]))

plt.plot(datax)
plt.plot(datay)
plt.show()

