import math
def function(x):
    return x**3-x-1
def differential(x):
    return 3*x**2-1
def main():
    x0, e = map(float, input().split())
    i=0
    while True:
        i+=1
        x1 = x0 - function(x0)/differential(x0)

        if abs(function(x1)) < e or abs(x1-x0)<e:
            break
        else:
            x0=x1
    print(f"Root = {x1}")
    print(f"Itarations = {i}")
if __name__=="__main__":
    main()