opcao = int(input("digite a opção desejada(1, 2 ou 3): "))
""""""
"consultar livro" "1"
"realizar emprestimo" "2"
"devolver livro" "3"
""""""
match opcao:
    case 1:
        print("você escolheu consuitar o livro.")
    case 2:
        print("você escolheu realiza um emprestimo.")
    case 3:
        print("você escolheu devolver o livro.")
    case _:
        print("opção não encontrada.")