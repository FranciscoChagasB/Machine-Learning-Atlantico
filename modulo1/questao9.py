# Crie uma função que recebe uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne
# a lista ordenada pelo nome das pessoas em ordem alfabética.

# Função que irá percorrer uma lista de tuplas e ordenar o atributo nome por ordem alfabética.
def ordenar_por_nome(lista_pessoas):
    # Variável com o tamanho da lista.
    tam = len(lista_pessoas)
    
    for i in range(tam - 1):
        for j in range(0, tam - i - 1):
            nome_atual = lista_pessoas[j][0]
            nome_seguinte = lista_pessoas[j + 1][0]

            # Compara os nomes individualmente até encontrar a primeira letra diferente
            k = 0
            while k < len(nome_atual) and k < len(nome_seguinte):
                if nome_atual[k] > nome_seguinte[k]:
                    lista_pessoas[j], lista_pessoas[j + 1] = lista_pessoas[j + 1], lista_pessoas[j]
                    break
                elif nome_atual[k] < nome_seguinte[k]:
                    break
                k += 1
    
    # Retorna a lista de pessoas ordenada
    return lista_pessoas

# Lista criada.
lista = [("João", 20), ("Ana", 21), ("Maria", 22), ("Carlos", 23), ("Bento", 25)]

# Lista que irá receber o valor da função, que neste caso é a lista ordenada alfabeticamente.
lista_ordenada = ordenar_por_nome(lista)

# Imprime a lista ordenada.
print("Lista em ordem alfabética:", lista_ordenada)