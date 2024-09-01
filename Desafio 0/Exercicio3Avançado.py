from itertools import combinations

def gerar_subconjuntos(vetor, max_size=None, min_size=0, distinct_only=False, sort_subsets=False):

    n = len(vetor)

    # Inicializa uma lista para armazenar todos os subconjuntos.
    subconjuntos = []

    # Ordena o vetor se sort_subsets for True
    if sort_subsets:
        vetor = sorted(vetor)

    # Remove elementos duplicados se distinct_only for True.
    if distinct_only:
        vetor = list(set(vetor))

    # Cria subconjuntos de todos os tamanhos possíveis
    for size in range(min_size, n + 1):
         # Se max_size foi fornecido e o tamanho atual excede max_size, pula para o próximo tamanho.
        if max_size is not None and size > max_size:
            continue
        # Gera todos os subconjuntos do tamanho atual e adiciona à lista de subconjuntos.
        for subset in combinations(vetor, size):
            subconjuntos.append(list(subset))

    # Ordena os subconjuntos se sort_subsets for True
    if sort_subsets:
        subconjuntos = [sorted(sub) for sub in subconjuntos]
        subconjuntos = sorted(subconjuntos)

    return subconjuntos

# Exemplo de uso
vetor = [1,2,3]

# Exemplos de Parâmetros:

# max_size=2 para gerar apenas subconjuntos com no máximo 2 números
# min_size=2 para gerar apenas subconjuntos com no mínimo 2 números
# distinct_only=True para gerar subconjuntos apenas com elementos distintos. Exemplo de vetor: vetor=[1,2,2,3]
# sort_subsets=True para gerar subconjuntos ordenados em ordem crescente. Exemplo de vetor: vetor=[3,1,2]

resultados = gerar_subconjuntos(vetor, sort_subsets=True)
print(resultados)
