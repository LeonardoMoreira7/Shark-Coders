import requests

url = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-USD")
cotacao = url.json()

cotacao_dolar = float(cotacao["EURUSD"]["bid"])
valor = float(input("Qual o valor em Dolares deseja converter? "))
resultado = valor / cotacao_dolar
print(f"O valor convertido é de {round(resultado,2)} euros.")