
from random import randint
from time import sleep
li = []
print("Bem vindo ao Slot Machine!\n 3 números iguais = Aposta x 50\n 2 números iguais = Aposta x 3\n 3 números diferentes = Perde o valor apostado")
while True:
    for x in range(3):
        n = randint(1,6)
        li.append(n)
    saldo = randint(100,200)
    print(f"O seu saldo atual é de {saldo} euros")

    montante = int(input("Digite o montante que deseja apostar: "))
    if montante <= 0:
        print("Montante inválido")
    else:
        print("Aperte ENTER para iniciar")
        print("Girando ...")
        sleep (3)
