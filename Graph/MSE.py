import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def f1(n):
    return (3*n+144)/(n-1)**2
def f2(n):
    return 3/n
def f3(n):
    return (3*n+144)/(n+1)**2

def Graph_MSE(f1,f2,f3):

    x = []
    y1 = []
    y2 = []
    y3 = []
    i = 2
    while(i<=100):
        x.append(i)
        y1.append(f1(i))
        y2.append(f2(i))
        y3.append(f3(i))
        i = i+1
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y1, color='tab:blue')
    ax.plot(x, y2, color='tab:orange')
    ax.plot(x, y3, color='tab:green')

    plt.show()
def main():
    print("MSE")
    Graph_MSE(f1,f2,f3)
if __name__ =="__main__":
    main()