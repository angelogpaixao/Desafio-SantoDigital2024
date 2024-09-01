from itertools import combinations

def gerar_subconjuntos(vetor):
    # Inicializa uma lista para armazenar todos os subconjuntos.
    subconjuntos = []
    
    # Itera sobre todos os tamanhos possíveis dos subconjuntos, de 0 a n.
    for r in range(len(vetor) + 1):
        # Gera todos os subconjuntos de tamanho r.
        for subset in combinations(vetor, r): # combinations é importado da biblioteca itertools e é usado para gerar todas as combinações possíveis de um dado comprimento.
            subconjuntos.append(list(subset))
    
    return subconjuntos

# Exemplo de uso

n = int(input('Digite a quantidade de números do conjunto: '))
vetor = []

for cont in range(1, n+1):
    vetor.append(int(input('Digite um numero: ')))

resultados = gerar_subconjuntos(vetor)
print(resultados)