def encontrar_menores_diferencas(vetor, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    menor = float('inf')
    pares = []

    # Ordena o vetor em ordem crescente.
    vetor.sort()

    # Calcula as diferenças entre números consecutivos
    for i in range(len(vetor) - 1):

        
        if not allow_duplicates and vetor[i] == vetor[i + 1]: # Se 'allow_duplicates' for False e os números consecutivos são iguais, ignora o par.
            continue

        diferenca = abs(vetor[i] - vetor[i + 1]) # Calcula a diferença absoluta entre o número atual e o próximo número.

        # Se a diferença calculada for menor que a menor diferença encontrada até agora,
        # atualiza a menor diferença e reinicializa a lista de pares.
        if diferenca < menor:
            menor = diferenca
            pares = [(vetor[i], vetor[i + 1])]

        # Se a diferença calculada for igual à menor diferença encontrada,
        # adiciona o par atual à lista de pares.
        elif diferenca == menor:
            pares.append((vetor[i], vetor[i + 1]))

    # Se 'sorted_pairs' for True, ordena os pares em ordem crescente.
    if sorted_pairs:
        pares = [sorted(par) for par in pares]

    # Se 'unique_pairs' for True, remove pares duplicados.
    if unique_pairs:
        pares_unicos = set()
        for par in pares:
            pares_unicos.add(tuple(sorted(par))) # Adiciona o par à coleção de pares únicos, garantindo que (a, b) e (b, a) sejam tratados como iguais.
        pares = list(pares_unicos)

    return pares

# Exemplo de uso
vetor = [3, 8, 3, 5, 10, 1, 8, 12]

pares_com_menor_diferenca = encontrar_menores_diferencas(vetor, allow_duplicates=False, sorted_pairs=True, unique_pairs=True)
print(pares_com_menor_diferenca)
