
def exercicio1():
    temps = [[24, 25, 26], [27, 28, 29], [21, 22, 25]]
    cids = ["São Paulo", "Curitiba", "Rio de Janeiro"]

    print("\nImpressão de Dados:")
    for j in range(3):
        print(f"Cidade: {cids[j]}")
        for i in range(3):
            print(f"Temperatura: {temps[j][i]}")

        media = calcularMedias(temps[j])
        print(f"Média de temperatura da cidade: {media:.2f}")

        TipoRoupa(media)

def TipoRoupa(p):
    if(p <= 18):
        print("Você deve usar roupa de frio!")
    elif(p >18 and p <= 24):
        print("Você deve usar roupa confortavel!")
    elif(p > 24):
        print("Você deve usar roupa de calor!")

def calcularMedias(tem):
    s = 0
    for x in range(3):
        s += tem[x]
    
    m = s/3
    return m
    
