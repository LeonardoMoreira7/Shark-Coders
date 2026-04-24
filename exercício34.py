with open('exemplo.txt', 'a') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)