if __name__=="__main__":
    n=int(input())
    for i in range(n):
        aux=input()
        aux=aux.split()
        a=int(aux[0])
        b=int(aux[1])
        if a>b:
            dividendo=a
            divisor=b
        else:
            dividendo=b
            divisor=a
        resto=dividendo%divisor
        while(dividendo%divisor!=0):
            resto=dividendo%divisor
            dividendo=divisor
            divisor=resto
        print(divisor)