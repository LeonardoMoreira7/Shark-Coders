def criar_ficheiro():
    nome = input("introduza um nome para um ficheiro novo: ")
    nome += ".txt"

    with open(nome, "w") as ficheiro:
        print(f"Ficheiro {nome} criado com sucesso")

criar_ficheiro()