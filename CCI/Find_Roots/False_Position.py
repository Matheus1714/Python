import math
def function(x):
    fx = x**3-x-1
    return fx
def main():
    a, b, e = map(float, input().split())
    i = 0
    while True:
        i+=1
        fxa=function(a)
        fxb=function(b)
        x=(a*fxb-b*fxa)/(fxb-fxa)
        fx=function(x)
        if abs(fxa) < e:
            x=a
            break
        elif abs(fxb) < e:
            x=b
            break
        elif abs(fx) < e:
            break
        elif fxa*fx<0:
            b=x
        elif fxa*fx >0:
            a=x
        elif b-a<e:
            x=(b+a)/2
    print(f"Root ={x}")
    print(f"Itaration = {i}")
if __name__=="__main__":
    main()