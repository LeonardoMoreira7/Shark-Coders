velocidade = int(input("Qual foi a velocidade?"))
if velocidade>80:
    print(f"Estás acima do limite permitido. A multa foi gerada no valor de {(velocidade-80)*2} euros")
else:
    print("Dentro do limite. Boa viagem!")