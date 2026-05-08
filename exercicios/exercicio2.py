def filtrar_por_sexo(lista_alunos, sexo):
    return [aluno for aluno in lista_alunos if aluno['sexo'].upper() == sexo.upper()]

def filtrar_por_nota(lista_alunos, nota_corte, acima=True):
    if acima:
        return [aluno for aluno in lista_alunos if aluno['nota'] >= nota_corte]
    return [aluno for aluno in lista_alunos if aluno['nota'] < nota_corte]

def obter_interseccao(lista_a, lista_b):
    """Retorna apenas os alunos que estão em ambas as listas."""
    # Comparamos os dicionários (ou um identificador único como nome)
    return [aluno for aluno in lista_a if aluno in lista_b]

def exercicio2():
    # 1. Entrada de Dados
    alunos = [
        {"nome": "Ana", "nota": 8.5, "sexo": "F"},
        {"nome": "Bruno", "nota": 6.0, "sexo": "M"},
        {"nome": "Carla", "nota": 9.0, "sexo": "F"},
        {"nome": "Daniel", "nota": 4.5, "sexo": "M"},
        {"nome": "Eduarda", "nota": 7.5, "sexo": "F"},
        {"nome": "Felipe", "nota": 10.0, "sexo": "M"},
        {"nome": "Gabriela", "nota": 5.5, "sexo": "F"},
        {"nome": "Henrique", "nota": 8.0, "sexo": "M"},
        {"nome": "Isabela", "nota": 6.5, "sexo": "F"},
        {"nome": "João", "nota": 3.0, "sexo": "M"},
    ]

    # 2. Processamento (Grupos Principais)
    mulheres = filtrar_por_sexo(alunos, "F")
    homens = filtrar_por_sexo(alunos, "M")
    aprovados = filtrar_por_nota(alunos, 7.0)
    reprovados = filtrar_por_nota(alunos, 7.0, acima=False)

    # 3. Processamento (Intersecções)
    mulheres_aprovadas = obter_interseccao(mulheres, aprovados)
    homens_aprovados = obter_interseccao(homens, aprovados)

    # 4. Exibição dos Resultados
    print("=== GRUPOS GERAIS ===")
    print(f"Mulheres: {len(mulheres)} | Homens: {len(homens)}")
    print(f"Aprovados: {len(aprovados)} | Reprovados: {len(reprovados)}")

    print("\n=== INTERSECÇÕES (Cruzamento de Dados) ===")
    print(f"Mulheres Aprovadas: {len(mulheres_aprovadas)}")
    for m in mulheres_aprovadas:
        print(f" - {m['nome']} (Nota: {m['nota']})")

    print(f"\nHomens Aprovados: {len(homens_aprovados)}")
    for h in homens_aprovados:
        print(f" - {h['nome']} (Nota: {h['nota']})")
