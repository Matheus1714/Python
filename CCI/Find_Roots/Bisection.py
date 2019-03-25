def function(x):
    return x**3-x-1

def main():
    e, inf, sup = map(float,input().split())

    k=0
    while(sup-inf>e):
        M=function(inf)
        x=(inf+sup)/2
        if(M*function(x)>0):
            inf=x
        else:
            sup=x
        k=k+1
    print(f'{inf} ----- {sup}')


if __name__=="__main__":
    main()