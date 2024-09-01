def gerar_lista_asteriscos(n):
    string = "*"
    aux = ""
    i = []
    
    for cont in range(1, n + 1):
        # Adiciona um asterisco à string auxiliar.
        aux = aux + string
        # Adiciona a string auxiliar (com os asteriscos acumulados) à lista.
        i.append(aux)

    return i


n = int(input('Digite um número: '))
lista_asteriscos = gerar_lista_asteriscos(n)
print(lista_asteriscos)