from random import randint
n1 = randint(1, 100)
jogadas = 0
while True:
    numero_jogador = int(input("Diz um número "))
    if numero_jogador == n1:
        print("Boa, acertaste!")
        break
    elif numero_jogador < n1:
        print("Mais")
        jogadas += 1
    elif numero_jogador > n1:
        print("Menos")
        jogadas += 1
print(f"Foram precisas {jogadas} jogadas até acertares!")