# import matplotlib.pyplot as plt
from math import sin
def f(x,y):
    return -3*y**2-y

def main():
    print("Runge Kutta")
    x0 = 0
    y0 = 1
    a = 0
    b = 1
    n = 10
    h = (b-a)/n

    Y = []
    X = []
    Y.append(y0)
    X.append(x0)
    y = y0
    x = x0

    print(f"pass: {h}")
    term = float(input("Input the x value: "))
    for i in range(n):
        k1 = f(x,y)
        k2 = f(x+h, y+h*k1)
        x = x + h
        y = y + (h/2)*(k1+k2)
        Y.append(y)
        X.append(x)
        if(x == term or int(x + 0.1) == term):
            print(f"y({ x }) = {y}")
            
    # plt.plot(X,Y)
    # plt.show()

if __name__ == "__main__":
    main()