from numpy import linalg as LA
def main():
    print("eigenvalues and eigenvectors")
    A = [[70,-45,10],[-25,60,-5],[12,-25,48]]
    Va,Da = LA.eig(A)
    print(f"eigenvalue: {max(Va)}")
    
    for i in range (len(Va)):
        if(Va[i] == max(Va)):
            print(f"eigenvector: {Da[i]}")
            break

    B = [[70,-45,10, 10],[-25,60,5, 64],[12,25,48, 15], [2,5,9,84]]
    Vb,Db = LA.eig(B)


    print(f"eigenvalue: {max(Vb)}")
    
    for i in range (len(Vb)):
        if(Vb[i] == max(Vb)):
            print(f"eigenvector: {Db[i]}")
            break
if __name__=="__main__":
    main()