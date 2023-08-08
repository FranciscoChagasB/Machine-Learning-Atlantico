# Escreva uma função que receba duas listas e retorne outra lista com os elementos que
# estão presentes em apenas uma das listas

# Função que irá verificar se um elemento de uma lista está em uma outra lista.
def diferenca_entre_listas (lista1, lista2):
    # Lista para armazenar os elementos diferentes.
    elementos_diferentes = []

    # Laço para verificar se o elemento não está na segunda lista.
    for elemento in lista1:
        if elemento not in lista2:
            elementos_diferentes.append(elemento)

    # Laço para verificar se o elemento não está na primeira lista.
    for elemento in lista2:
        if elemento not in lista1:
            elementos_diferentes.append(elemento)

    # Retorna a lista com todos elementos diferentes.
    return elementos_diferentes

# Listas criadas.
lista1 = [1, 2, 3, 9, 10, 11, 12, 13, 14]
lista2 = [1, 2, 3, 4, 5, 6, 13, 14, 15]

# Lista que irá receber o valor da função, que neste caso é a lista com os elementos diferentes da lista1 e lista2.
elementos_diferentes = diferenca_entre_listas(lista1, lista2)

# Imprime a lista com os elementos diferentes.
print(elementos_diferentes)