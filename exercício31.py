from random import randint
saldo = randint(100,200)
cartas = randint(2,10)
banca = 0
while True:
    print(f"O seu saldo atual é de {saldo} euros")
    montante = int(input("Digite o montante que deseja apostar: "))
    print(f"Tens {cartas} pontos")
    while True:
        opc = int(input("Deseja comprar mais cartas?"))
        if opc == 1:
            cartas += randint(2, 10)
            print(f"Estás com {cartas} pontos\n")
            if cartas > 21:
                print()
                print("Perdeste, tenta outra vez!")
                break
        elif opc == 2:
            banca = randint(15,21)
            print(f"A banca somou {banca} pontos")
            if cartas > banca:
                print()
                ganhos = montante * 2
                saldo += ganhos
                print("Ganhaste!\n")
                print(f"O saldo atual é {saldo} euros")
                break
            elif cartas < banca:
                print()
                saldo = saldo - montante
                print("Perdeste!\n")
                print(f"O saldo atual é {saldo} euros")
                break
            else:
                print()
                print("Foi um empate!\n")
                break