from random import randint
jogadas = 0
while True:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    if dado1 == dado2:
        print(dado1, "Este é o resultado dos dados")
        break
    else:
        jogadas += 1
print(f"Foram precisas {jogadas} jogadas para aparecer dois dados iguais")