# Dada uma lista contendo números inteiros, como você encontraria o maior número
# e o menor número dessa lista em uma única passagem.

def maiornum_menornum(lista):
    # Verifica se a lista está vazia.
    if len(lista) == 0:
        return None, None
    
    # Inicializa o maior e o menor número com o primeiro elemento da lista.
    maior = menor = lista[0]  
    
    # Percorre a lista verificando e atualizando o maior e o menor valor.
    for numero in lista[1:]:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    
    # Retorna o maior e o menor valor da lista.
    return maior, menor

# Lista criada.
lista = [12, 34, 7, 23, 40, 15, 11, 5, 2, 30]

# Lista que irá receber o valor da função, que neste caso é maior e o menor número de uma lista.
maiornum, menornum = maiornum_menornum(lista)

# Imprime o maior e o menor número.
print("O maior número é:", maiornum, "e o menor número é:", menornum)