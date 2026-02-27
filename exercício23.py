import random

opcoes = ["pedra", "papel", "tesoura"]

def determinar_vencedor(jogador, computador):
    if 

while True:
    jogador_escolha = input("Escolhe pedra, papel ou tesoura (ou 'sair' para terminar): ").lower()

    if jogador_escolha == "sair":
        print("Obrigado por jogar!")
        break
    elif jogador_escolha not in opcoes:
        print("Escolha inválida.")
        continue

    resultado = random.choice(opcoes)
    print(f"Computador escolheu: {resultado}")

    resultado_jogo = determinar_vencedor(jogador_escolha, resultado)
    print(resultado_jogo)