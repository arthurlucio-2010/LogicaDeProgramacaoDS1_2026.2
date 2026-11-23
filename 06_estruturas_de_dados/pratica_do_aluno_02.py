#Crie uma matriz 2x2 contendo números inteiros e calcule a soma de todos os 4 elementos utilizando dois laços `
# for` aninhados.

# TODO: Crie o dicionário do veículo e percorra com for
veiculo = {}

# Escreva o laço for com .items()

matriz = [
    [20 , 30],
    [30 , 40]
]

soma = 0 


for linha in matriz:
    for numero in linha :
        soma += numero

print("A soma dos elementos é:", soma)