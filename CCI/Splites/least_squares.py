import matplotlib.pyplot as plt

def func(x):
    return 1526.099566*x+8613.456429

def averange(y):
    a = 0
    for i in range(len(y)):
        a = a + y[i]
    return a/len(y)

def standard_deviation(y, a):
    s = 0
    for i in range(len(y)):
        s = s + (abs(y[i]-a))**2
    return s

def standard_error_estimate(x,y):
    s = 0
    for i in range(len(x)):
        s = s + (abs(func(x[i])-y[i]))**2
    return s

def main():
    print("Least Square")
    x = list(range(10,90,10))
    y = [25,70,380,550,610,1220,830,1450]
    a = averange(y)

    st = standard_deviation(y,a)
    sr = standard_error_estimate(x, y)

    sy = (st/(len(x)-1))**(1/2)

    syx = (sr/(len(x)-2))**(1/2)

    r = (abs(st-sr)/st)**(1/2)

    print(sy)
    print(syx)
    print(r)

if __name__=="__main__":
    main()