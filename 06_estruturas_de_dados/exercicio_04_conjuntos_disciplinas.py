"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web = {"joao", "carlos", "mario", "major"}

alunos_banco = {"joao", "carlos", "paje", "tabajara"}

intersecao = alunos_web & alunos_banco
print(intersecao)

diferenca = (alunos_web - alunos_banco)
print(diferenca)

