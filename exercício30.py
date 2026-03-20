from random import randint
from time import sleep
saldo = randint(100,200)
print("Bem vindo ao Slot Machine!\n 3 números iguais = Aposta x 50\n 2 números iguais = Aposta x 3\n 3 números diferentes = Perde o valor apostado")
while True:
    li = []
    for x in range(3):
        n = randint(1,6)
        li.append(n)
    print(f"O seu saldo atual é de {saldo} euros")

    montante = int(input("Digite o montante que deseja apostar: "))
    if montante <= 0:
        print("Montante inválido")
    else:
        input('Aperte ENTER para iniciar')
        print("Girando ...")
        sleep (3)
        for x in li:
            print([x], end='')
            sleep(2)
        if li[0] == li[1] or li[0] == li[2] or li [1] == li[2]:
            saldo = montante * 3
            print()
            print("Acertou 2!")
        elif li[0] == li[1] == li[2]:
            saldo = montante * 50
            print()
            print("JAKPOT!")
        else:
            saldo = saldo - montante
            print()
            print("Perdeu, tente outra vez!")