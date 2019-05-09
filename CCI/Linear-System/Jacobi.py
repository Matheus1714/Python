from numpy import array
def jacobi(ord, A, X, b, e):
    deltaX=[]
    C=[]
    g=[]
    X1=[]
    k=1
    for i in range(ord):
        line = []
        for j in range(ord):
            if i==j:
                line.append(0)
                g.append(b[i]/A[i][i])
            else:
                line.append(-A[i][j] / A[i][i])
        C.append(line)
    for i in range(ord):
            X1.append(0)
            deltaX.append(0)
    while(1):
        for i in range(ord):
            X1[i]=0
            deltaX[i]=0
        # X1=C*X+g;
        for l in range(ord):
            for c in range(ord):
                X1[l]=X1[l]+C[l][c]*X[c]
            X1[l]=X1[l]+g[l]
        for i in range(ord):
            deltaX[i]=X1[i]-X[i]
            if(deltaX[i]<0):
                deltaX[i]=-deltaX[i]
        dr1 = max(X1, key=float)
        dr2 = max(deltaX, key=float)
        dr = dr2/dr1
        if(dr<e):
            break
        for i in range(ord):
            X[i]=X1[i]
        k=k+1
    print(k)
    print(X1)
    print(dr)
            
def main():
    ord = 3
    A = [[3.0,-0.1, -0.2],[0.1,7.0,-0.3],[0.3,-0.2,10.0]]
    b = [7.85, -19.3, 71.4]
    X = [0.0,0.0,0.0]
    e=0.05

    jacobi(ord, A, X, b, e)
    
if __name__=="__main__":
    main()