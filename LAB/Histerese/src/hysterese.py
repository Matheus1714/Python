import matplotlib.pyplot as plt

def post_dados():
    file = open('../data/dados.txt', 'r')

    dados = []
    I = []
    H = []
    while True:
        line = file.readline()
        if line == '': break
        
        i, h = map(float, line.split())

        I.append(i)
        H.append(h)
    file.close()
    dados.append(I)
    dados.append(H)
    return dados

def draw_dados(dados):
    plt.plot(dados[0], dados[1])
    plt.show()


def main():
    print("Hysterese")
    dados = post_dados()

    draw_dados(dados)
if __name__=="__main__":
    main()