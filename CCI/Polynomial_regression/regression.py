from numpy.linalg import inv
from math import sqrt
import matplotlib.pyplot as plt

def main():
    print("Polynomial regression")
    #Initial Terms
    n=6
    m=2
    X = [1,2,3,4,5,6]
    Y = [1.487,2.9858,5.602,8.003,11.452,13.021]

    #Sum of x and y
    sum_x = 0
    sum_y = 0
    for i in range(n):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]
    #Sum of powers of x
    sum_x2 = 0
    sum_x3 = 0
    sum_x4 = 0
    sum_xy = 0
    sum_x2y = 0
    for i in range(n):
        sum_x2 = sum_x2 + X[i]**2
        sum_x3 = sum_x3 + X[i]**3
        sum_x4 = sum_x4 + X[i]**4
        sum_xy = sum_xy + X[i]*Y[i]
        sum_x2y = sum_x2y + (X[i]**2)*Y[i]
    #Averege
    x_a = sum_x/n
    y_a = sum_y/n

    #matrix Mc and Mb
    Mc = [[ n, sum_x, sum_x2 ], [ sum_x, sum_x2, sum_x3 ], [ sum_x2, sum_x3, sum_x4 ]]
    Mb = [ sum_y, sum_xy, sum_x2y]

    #Coeficients vector
    inv_Mc = inv(Mc)
    a = []
    for i in range(3):
        line = 0
        for j in range(3):
            line = line + inv_Mc[i][j]*Mb[j]
        a.append(line)

    #Polynomial
    y1 = []
    for i in range(n):
        line = 0
        for j in range(3):
            line = line + a[j]*X[i]**(j)
        y1.append(line)

    #Terms St and Sr
    St = 0
    Sr = 0
    for i in range(n):
        St = St + (Y[i]-y_a)**2
        Sr = Sr + (Y[i]-a[0]-a[1]*X[i]-a[2]*X[i]**2)**2
    Sy_x = sqrt(Sr/(n-(m+1)))
    
    #Cd terms
    Cd = (St - Sr)/St

    print(f"a0: {a[0]}")
    print(f"a1: {a[1]}")
    print(f"a2: {a[2]}")
    print(f"Cd: {Cd}")

    #Plots
    plt.plot( X, Y, 'go') 
    plt.plot( X, Y, 'k:', color='orange') 

    plt.plot( X, y1, 'r^')
    plt.plot( X, y1, 'k--', color='blue')

    plt.title("Polynomial Regression")

    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if __name__=="__main__":
    main()