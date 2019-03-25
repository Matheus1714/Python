def function(x):
    return x**3-x-1
def main():
    x0, x1, e =map(float, input().split())
    i=0
    while True:
        i+=1
        x1 = x0 - function(x0)*(x1-x0)/(function(x1)-function(x0))
        if(abs(function(x1))<e or abs(x1-x0)<e):
            break
    print(f"Root = {x1}")
    print(f"Iterators = {i}")
if __name__=="__main__":
    main()