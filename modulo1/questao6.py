# Escreva uma função que recebe uma lista de números e retorne outra lista com os números primos presentes.

# Função que irá verificar se um número é primo.
def numeros_primos(lista):
    # Lista para armazenar os números primos.
    numeros_primos = []

    for numero in lista:
        # Números primos são maiores que 1.
        if numero > 1:
            primo = True

            # Percorre de 2 até a raiz quadrada do número
            for i in range(2, int(numero ** 0.5) + 1):
                # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada, caso sim, não é primo
                if numero % i == 0:
                    primo = False
                    break
            
            # Se a variável primo ainda for True, o número é primo
            if primo:
                numeros_primos.append(numero)

    # Retorna a lista com todos números primos.
    return numeros_primos

# Lista criada.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Lista que irá receber o valor da função, que neste caso é a lista com os números primos.
numeros_primos = numeros_primos(lista)

# Imprime a lista com os números primos.
print(numeros_primos)
