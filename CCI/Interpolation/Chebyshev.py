from math import pi
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, polyfit, polyval

def f(x):
    return 3.0/(5.0+2.0*x**2)
def function_chebyshev(x,p):
    k=[]
    for i in range(p):
        k.append(-3.0*np.cos(i*pi/100))
    return k
def max_err(f1, f2, p):
    err=[]
    for i in range(p):
        err.append(f1[i] - f2[i])
        if(err[i]<0):
            err[i] = - err[i]
    return max(err, key=float)
def main():
    #Nodes
    node = int(input("Node:"))

    points = 100
    #Obtaining vector x with 100 divisions between [-3,3]
    xp = np.linspace(-3,3,points)
    #Get f (x) for each of the 100 points obtained
    f_x = f(xp)
    #p(x)
    p = np.polyfit(xp, f_x,node)
    #p(x) for each of the 100 points obtained
    p_x = np.polyval(p,xp)
    print(p)
    #g(x) are the nodes of Chebyshev for each of the 100 points obtained
    g_x = function_chebyshev(xp, points)
    #greater absolute error between the 100 points of f(x) and p(x)
    err_f_and_p = max_err(f_x, p_x, points)
    print(err_f_and_p)
    #Graph
    plt.plot(xp, f_x, label='f(x)')
    plt.plot(xp, p_x, label='p(x)')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title("Chebyshev Method")

    plt.legend()

    plt.show()
if __name__=="__main__":
    main()