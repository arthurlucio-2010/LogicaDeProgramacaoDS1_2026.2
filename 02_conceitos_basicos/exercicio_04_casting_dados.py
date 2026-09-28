"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
ano_de_nacimento = input ("digite seu ano de nacimento: ")
ano_de_nacimento = int (ano_de_nacimento)
idade = 2026 - ano_de_nacimento
print(f"você tera {idade} anos ate o fim de 2026> ")
