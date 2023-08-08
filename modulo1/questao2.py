# Escreva um programa que leia números digitados pelo usuário e pare quando o número 0 for digitado.
# No final, imprima a média dos números digitados.

# Lista para armazenar os números digitados.
numeros_digitados = []

# Entra no laço while até que o usuário insira o número 0.
while True:
    numero = int(input("Digite um número (digite 0 para parar): "))
    if numero == 0:
        break
    # Cada número inserido é armazenado na lista 'numeros_digitados'.
    numeros_digitados.append(numero)

# Calcula a soma da lista 'numeros_digitados' e armazena na variável 'soma'.
soma = sum(numeros_digitados)

# Calcula o tamanho da lista 'numeros_digitados' e armazena na variável 'tam'.
tam = len(numeros_digitados)

# Imprime a média da lista.
print("A média dos números digitados é: ", soma / tam)