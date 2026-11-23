#Crie um dicionário representando um veículo com as chaves `"marca"`, `"modelo"` e `"ano"`. 
# Imprima cada chave e seu respectivo valor usando o método `.items()` em um laço `for`.
# TODO: Crie o dicionário do veículo e percorra com for


# Escreva o laço for com .items()

veiculo = {
    "marca" : "corola",
    "modelo" : "onix",
    "ano": 2023
}
for chave, valor in veiculo.items():
    print(chave , valor)
    