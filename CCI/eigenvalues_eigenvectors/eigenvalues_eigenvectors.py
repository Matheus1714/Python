from numpy import linalg as LA
def main():
    print("eigenvalues and eigenvectors")
    A = [[70,-45,10],[-25,60,-5],[12,-25,48]]
    Va,Da = LA.eig(A)
    print(Va)
    print(Da)

    B = [[70,-45,10, 10],[-25,60,5, 64],[12,25,48, 15], [2,5,9,84]]
    Vb,Db = LA.eig(B)
    print(Vb)
    print(Db)
if __name__=="__main__":
    main()