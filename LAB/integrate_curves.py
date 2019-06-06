import numpy as np
import matplotlib.pyplot as plt

def dy(y,a):
    return a*y - y**3

def main():
    print("integrate curves")
    y = []
    x = []
    a = 0
    for i in range(100):
        y.append(dy(i,a))
        x.append(i)
    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    main()