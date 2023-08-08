# Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

# Função que irá verificar se um número é ímpar.
def retorna_impar(lista):
    # Lista para armazenar os números ímpares.
    lista_impar = []

    for numero in lista:
        # Verifica se o resto da divisão do número por 2 é 0, caso nao, é um número impar e deve ser armazenado.
        if((numero % 2 != 0)):
            lista_impar.append(numero)

    # Retorna a lista com todos números ímpares.
    return lista_impar

# Lista criada.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Lista que irá receber o valor da função, que neste caso é a lista com os números ímpares.
lista_impar = retorna_impar(lista)

# Imprime a lista com os números ímpares.
print(lista_impar)