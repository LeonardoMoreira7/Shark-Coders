import requests

lista = ["EUR", "USD", "BRL"]

print("=-"*10)
print("Coversor de Moedas")
print("=-"*10)

origem = int(input("Qual a moeda de origem? \n 0 - Euro \n 1 - Dólar Americano \n 2 - Real Brasileiro \n Escolha a opção: "))
origem = lista[origem]

print()
valor = int(input("Qual valor deseja converter: "))
print()

para = int(input("Para qual moeda deseja converter? \n 0 - Euro \n 1 - Dólar Americano \n 2 - Real Brasileiro \n Escolha a opção: "))
para = lista[para]
print()

cotacao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{origem+"-"+para}")
cotacao = cotacao.json()
cotacao_moeda = float(cotacao[origem+para]["bid"])

resultado = round(valor * cotacao_moeda, 2)
print(f"O valor convertido é de {resultado} {para}")