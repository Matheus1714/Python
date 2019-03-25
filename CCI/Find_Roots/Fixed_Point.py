import math
def function(x):
    return x**3-x-1
def Wx(x):
    return (x+1)**(1/3)
def main():
    x0, e = map(float, input().split())
    i=0
    while True:
        i+=1
        x1=Wx(x0)
        if abs(function(x1)) < e or abs(x1-x0) <e:
            print(f"x = {x1}")
            print(f"Number of iterations = {i}")
            break
        x0=x1
if __name__=="__main__":
    main()