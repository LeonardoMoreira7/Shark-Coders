def ler_ficheiro():
    with open("teste2.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        print(conteudo)

def procurar():
    texto = input("Qual a palavra que procuras?")
    with open("teste2.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            if texto in linha:
                print(linha.rstrip())

def contar():
    soma = 0
    with open("teste2.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            soma += 1

    print(f"Número de linhas no ficheiro: {soma} ")


ler_ficheiro()
procurar()
contar()