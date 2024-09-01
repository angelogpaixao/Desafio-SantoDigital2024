def encontrar_menores_diferencas(vetor):
    menor = float('inf')
    pares = []

    # Ordena o vetor em ordem crescente.
    vetor.sort()

    # Calcula as diferenças entre números consecutivos
    for i in range(len(vetor) - 1):
        diferenca = abs(vetor[i] - vetor[i + 1])

        # Se a diferença calculada for menor que a menor diferença encontrada até agora,
        # atualiza a menor diferença e reinicializa a lista de pares.
        if diferenca < menor:
            menor = diferenca
            pares = [(vetor[i], vetor[i + 1])]

        # Se a diferença calculada for igual à menor diferença encontrada,
        # adiciona o par atual à lista de pares.
        elif diferenca == menor:
            pares.append((vetor[i], vetor[i + 1]))

    return pares

# Exemplo de uso
n = int(input('Digite a quantidade de números: '))
vetor = []

for cont in range(1, n+1):
    vetor.append(int(input('Digite um numero: ')))

pares_com_menor_diferenca = encontrar_menores_diferencas(vetor)
print(pares_com_menor_diferenca)