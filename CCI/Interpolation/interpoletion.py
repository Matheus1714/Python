import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, polyfit, polyval

def function(x, func,  p):
    k=[]
    for i in range(p):
        k.append(np.polyval(func,x[i]))
    return k
def max_err(f1, f2, p):
    err=[]
    for i in range(p):
        err.append(f1[i] - f2[i])
        if(err[i]<0):
            err[i] = - err[i]
    return max(err, key=float)
    
def main():
    points = 100
    #Function definition f
    f = [1,0,0,0,0,0,0,0,-3,0,-2]
    #Obtaining vector x with 100 divisions between [-1,0]
    xp = np.linspace(-1,0,points)
    #Get f (x) for each of the 100 points obtained
    f_x = function(xp, f, points)
    #Function definition g
    g = [-1.004, 0.996, -2]
    #g (x) for each of the 100 points obtained
    g_x = function(xp, g, points)
    #p (x) of degree 2 that interpolates the 100 points [x, f (x)]
    p = np.polyfit(xp,f_x,2)
    #p (x) for each of the 100 points obtained
    p_x = function(xp, p, points)
    #greater absolute error between the 100 points of f (x) and g (x)
    err_f_and_g = max_err(f_x, g_x, points)
    print(err_f_and_g)
    #greater absolute error between the 100 points of f (x) and p (x)
    err_f_and_p = max_err(f_x, p_x, points)
    print(err_f_and_p)
    #Graph
    plt.plot(xp,f_x, label='f(x)')
    plt.plot(xp, g_x, label='g(x)')
    plt.plot(xp, p_x, label='p(x)')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title("Interpolate Method")

    plt.legend()

    plt.show()
if __name__=="__main__":
    main()
