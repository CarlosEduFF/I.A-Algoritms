
def exercicio1():

    temps = [[24, 25, 26], [27, 28, 29], [21, 22, 25], [11,12,17],[17,20,26]]

    cids = ["São Paulo", "Curitiba", "Rio de Janeiro", "Lomdrina", "Fortaleza"]

    print("\nImpressão de Dados:")

    medias = {}

    print("\nImpressão de Dados:")

    for j in range(len(cids)):

        cidade = cids[j]

        print(f"Cidade: {cidade}")

        for i in range(3):
            print(f"Temperatura: {temps[j][i]}")

        media = calcularMedias(temps[j])

        medias[cidade] = media

        print(f"Média da cidade: {media:.2f}")

        TipoRoupa(media)

        print("---------------------------")

    cidade_mais_quente = max(medias, key=medias.get)
    cidade_mais_fria = min(medias, key=medias.get)

    print("\n=== Estatísticas Gerais ===\n")

    print(f"Cidade mais quente: {cidade_mais_quente} ({medias[cidade_mais_quente]:.2f})")

    print(f"Cidade mais fria: {cidade_mais_fria} ({medias[cidade_mais_fria]:.2f})")

    media_geral = sum(medias.values()) / len(medias)

    print(f"Média geral das cidades: {media_geral:.2f}")

def TipoRoupa(p):
    if(p <= 18):
        print("Você deve usar roupa de frio!")
    elif(p >18 and p <= 24):
        print("Você deve usar roupa confortavel!")
    elif(p > 24):
        print("Você deve usar roupa de calor!")

def calcularMedias(tem):
    soma = 0
    for x in range(3):
        soma += tem[x]
    
    m = soma/3
    return m
    
