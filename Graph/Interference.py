import matplotlib.pyplot as plt
import numpy as np

def f(dy):
    return (np.sin(377*dy))**2/(377*dy)**2
def main():
    print("Interference")
    interval = 2000
    i = -interval
    x = []
    y = []
    di = 1
    while(i<interval):
        x.append(i)
        y.append(f(i))
        i = i + di
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, color='tab:blue')

    plt.show()

if __name__=="__main__":
    main()