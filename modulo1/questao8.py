# Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor da lista.

# Função que irá percorrer todos elementos de uma lista e verificar qual o segundo maior elemento.
def segundo_maior_valor(lista):
    # Variável com o tamanho da lista.
    tam = len(lista)
    
    # Algorítmo Bubble Sort para ordenar a lista
    for i in range(tam - 1):
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    # Se a lista tem 1 ou nenhum elemento não existe um segundo maior, então retorna 'None'.
    if len(lista) < 2:
        return None
    
    # Retorna o segundo maior valor, ou seja, o penúltimo elemento na lista.
    return lista[-2]

# Lista criada.
lista = [12, 34, 7, 23, 40, 15]

# Lista que irá receber o valor da função, que neste caso é o segundo maior valor de uma lista.
segundo_maior = segundo_maior_valor(lista)

# Imprime o segundo maior valor da lista.
print("O segundo maior valor é:", segundo_maior)