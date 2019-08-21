#---------------------------------------------------------------------------------#
#Libs used#
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
#---------------------------------------------------------------------------------#
#Get elements of the files#
G = np.genfromtxt('info.csv',delimiter=',', dtype= [('x', float), ('y', float)])
G.sort(order='y')
#---------------------------------------------------------------------------------#
#Separate columns#
f = []
V = []
for g in G:
    f.append(g[1])
    V.append(g[0])
#---------------------------------------------------------------------------------#
#Interpolation#
F = interp1d(f, V)
#---------------------------------------------------------------------------------#
#Drawing Figure#
xnew = np.arange(min(f),max(f), 0.1)
ynew = F(xnew)   # use interpolation function returned by `interp1d`

print('resonant frequency: ',max(F(xnew)))

plt.plot(f, V, 'o', xnew, ynew, '-')

plt.xlabel('f(Hz)')
plt.ylabel('V(V)')
plt.title('Diagram')
plt.show()
#---------------------------------------------------------------------------------#