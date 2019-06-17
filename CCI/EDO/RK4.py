import matplotlib.pyplot as plt
from math import sin
def f(x,y):
    return 4*sin(0.8*x) - 0.5*y

def main():
    print("Runge Kutta")
    x0 = 0
    y0 = 2
    a = 0
    b = 1
    n = 200
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
        k2 = f(x+h/2, y+h*k1/2)
        k3 = f(x+h/2, y+h*k2/2)
        k4 = f(x+h, y + h*k3)
        x = x + h
        y = y + (h/6)*(k1+2*k2+2*k3+k4)
        Y.append(y)
        X.append(x)
        if(x == term):
            print(f"y({ x }) = {y}")

    # plt.plot(X,Y)
    # plt.show()

if __name__ == "__main__":
    main()