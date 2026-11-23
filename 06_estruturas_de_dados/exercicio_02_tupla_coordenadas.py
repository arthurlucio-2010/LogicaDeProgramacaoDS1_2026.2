"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:

cidades = ("tiangua", "sao benedito")

try:
    cidades[1] = "Ubajara"

except TypeError:
    print("erro: nao e possivel alterauma tupa, pois ela e imutavel.")
    print(cidades)
    print("não foi possível adicionar a cidade")