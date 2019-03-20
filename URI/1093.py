def gambler(n1, n2, at):
    dado=0
    if at == 3:
        return n1/(n1+n2)
    else:
        dado = 1.0 - (6-at)/6.0
        dado = (1 - dado)/dado
        return (1 - dado**n1)/(1 - dado**(n1+n2))

if __name__=="__main__":
    while(1):
        aux=input()
        aux=aux.split()
        EV1=int(aux[0])
        EV2=int(aux[1])
        AT=int(aux[2])
        D=int(aux[3])

        if(EV1==0 and EV2==0 and AT==0 and D==0):
            break
        aux = EV1
        EV1=0
        while(aux>0):
            aux=aux-D
            EV1=EV1+1
        aux=EV2
        EV2=0
        while(aux>0):
            aux=aux-D
            EV2=EV2+1
        p=gambler(EV1,EV2,AT)
        p=100*p

        print(round(p,1))
