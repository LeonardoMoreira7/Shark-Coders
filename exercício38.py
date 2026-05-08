def cadastro():
    nome = input("Indique um nome: ")
    idade = int(input("Indique uma idade: "))
    with open("Lista_Idades.txt", "a") as ficheiro:
        ficheiro.write(nome + "\n")
        ficheiro.write(str(idade) + "\n")

def buscar():
    nome = input("Indique o nome que procura: ")
    with open("Lista_Idades.txt", "r") as ficheiro:
        for linha in ficheiro:
            if nome in linha:
                print("Idade: " + ficheiro.readline())

print("-=" *12)
print("Manipulação de Arquivos")
print("-=" *12)
print()

while True:
    print("0 - Sair \n 1 - Cadastrar \n 2 - Buscar")
    opcao = int(input("Opção desejada: "))
    if opcao == 0:
        print("Obrigado por utilizar o programa")
        break
    elif opcao == 1:
        print()
        cadastro()
    elif opcao == 2:
        print()
        buscar()
    else:
        print("Opção Inválida")