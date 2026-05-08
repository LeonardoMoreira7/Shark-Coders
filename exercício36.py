def criar_ficheiro():
    nome = input("introduza um nome de um ficheiro existente: ")
    nome += ".txt"

    with open(nome, "r", encoding="utf-8") as ficheiro:

        conteudo = ficheiro.read()
        print(conteudo)

criar_ficheiro()