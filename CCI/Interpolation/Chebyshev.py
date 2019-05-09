from math import pi
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, polyfit, polyval

def f(x):
    return 3/(5+2*x**2)
def function(x, func,  p):
    k=[]
    for i in range(p):
        k.append(np.polyval(func,x[i]))
    return k
def function_chebyshev(x,p):
    k=[]
    for i in range(p):
        k.append(-3*np.cos(i*pi/2))
    return k

def main():
    points = 100
    #Obtaining vector x with 100 divisions between [-3,3]
    xp = np.linspace(-3,3,points)
    #Get f (x) for each of the 100 points obtained
    f_x = f(xp)
    #p(x)
    p = np.polyfit(xp, f_x,2)
    #p (x) for each of the 100 points obtained
    p_x = function_chebyshev(xp, points)
    #Graph
    plt.plot(xp,f_x, label='f(x)')
    plt.plot(xp, p_x, label='p(x)')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title("Chebyshev Method")

    plt.legend()

    plt.show()
if __name__=="__main__":
    main()