import matplotlib.pyplot as plt

h = 6.63
k = 1.38
c = 3
e = 2.718
T = 3000

def f(_lambda):
    _f = _lambda/c
    x = h/(k*T) * (_f)
    var = 
    return var * x**3/(e**x-1)

def main():
    print("Planck")

    x = []
    y = []
    i = 180
    di = 100
    while(i<=10**5):
        x.append(i)
        y.append(f(i))
        i = i + di
    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    main()