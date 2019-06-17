import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy import trapz

def f(x):
    return 2 + 5*x - 3*x**2 + 6*x**3 - 7*x**4 - 3*x**5 + x**6
def E(space, inf, sup):
    F=[]
    h = (sup-inf)/space
    for i in range(space+1):
        F.append(f(inf+i*h))
    return F
def main():
    print("trapeze rule")
    a = 0
    b = 1
    space = int(input("Segments: "))
    h = (b-a)/space
    y = E(space,a,b)
    Ia = trapz(y,dx=h)

    I, Ea = quad(f, a, b)
    Et = I - Ia

    print(f"I: {I}")
    print(f"Ia: {Ia}")
    print(f"Et: {Et}")
    print(f"Ea: {Ea}")

if __name__=="__main__":
    main()