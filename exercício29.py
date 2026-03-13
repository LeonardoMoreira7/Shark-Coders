from random import randint
from time import sleep
vida1 = 20
vida2 = 20
while True:
    forca1 = randint(1, 5)
    forca2 = randint(1, 5)
    if vida1 <= 0:
        print("O jogador 2 venceu!")
        break
    elif vida2 <= 0:
        print("O jogador 1 venceu!")
        break
    else:
        vida1 = vida1 - forca2
        print(f"O jogador 2 deu um murro de força {forca2} e a vida do jogador 1 foi para {vida1}")
        sleep(1)
        vida2 = vida2 - forca1
        print(f"O jogador 1 deu um murro de força {forca1} e a vida do jogador 2 foi para {vida2}")
        sleep(1)