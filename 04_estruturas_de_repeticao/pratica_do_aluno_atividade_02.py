# TODO: Desenvolva o acumulador com parada no 0

# Escreva a estrutura de repetição while
soma = 0
while True:
    numero = float(input("digite um numero(0 para encerrar): "))
    if numero == 0:
        break
        soma += numero
print("A soma dos numeros é: ")
