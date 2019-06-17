from math import log10, sqrt
import matplotlib.pyplot as plt

def main():
    print("Exponential Model")
    #Initial Terms
    n=6
    X = [1,2,3,4,5,6]
    Y = [1.487,2.9858,5.602,8.003,11.452,13.021]
    #Log10 Transformation
    W=[]
    Z=[]
    for i in range(n):
        W.append(log10(X[i]))
        Z.append(log10(Y[i]))
    #Sum Terms
    sum_w = 0
    sum_z = 0
    for i in range(n):
        sum_w = sum_w + W[i]
        sum_z = sum_z + Z[i]
    
    #Quadratic sum
    quad_sum_w = 0
    sum_wz = 0
    for i in range(n):
        quad_sum_w = quad_sum_w + W[i]**2
        sum_wz = sum_wz + W[i]*Z[i]
    
    #Averege
    w_a = sum_w/n
    z_a = sum_z/n

    #Terms a0 and a1
    a1 = ( n * sum_wz - sum_w*sum_z)/( n * quad_sum_w - sum_w**2 )
    a0 = z_a -a1*w_a

    #Terms alpha end bertha
    alpha = 10**a0
    betha = a1

    #Coordinates Y1 and Y2
    y1 = []
    y2 = []
    for i in range(n):
        y1.append(a1*X[i]+a0)
        y2.append(alpha*X[i]**betha)
    
    #St and Sr
    St = 0
    Sr = 0
    for i in range(n):
        St = St + (Z[i] - z_a)**2
        Sr = Sr + (Z[i] - a0 - a1*W[i])**2
    Sy = sqrt(St/(n-1))
    Sy_x = sqrt(Sr/(n-2))

    #Cd and r
    Cd = (St - Sr)/St
    r = sqrt(Cd)
    #Prits

    print(f"a0: {a0}")
    print(f"a1: {a1}")
    print(f"alpha: {alpha}")
    print(f"betha: {betha}")
    print(f"Cd: {Cd}")
    print(f"r: {r}")

    #plots

    plt.plot( X, Y, 'go') 
    plt.plot( X, Y, 'k:', color='orange') 

    plt.plot( X, y1, 'r^')
    plt.plot( X, y1, 'k--', color='blue') 

    plt.plot( X, y2, 'r^')
    plt.plot( X, y2, 'k--', color='red')

    plt.title("Exponential Model")

    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__=="__main__":
    main()