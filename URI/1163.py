import math
g=9.80665
if __name__=="__main__":
    h = float(input())
    p1,p2 = map(int,input().split())
    n=int(input())
    for i in range(n):
        a, v = map(float,input().split())
        a=a*math.pi/180
        xmin=v*math.cos(a)*(v*math.sin(a)-math.sqrt(v**2*math.sin(a)+2*g*h))/g
        xmax=v*math.cos(a)*(v*math.sin(a)+math.sqrt(v**2*math.sin(a)+2*g*h))/g
        
        if(xmin>=p1 or xmin <=p2 or xmax >=p1 or xmin <= p2):
            print(f'{xmax} -> DUCK', xmax)
        else:
            print(f'{xmax} -> NUCK', xmax)