kwh = int(input("Qual é a quantidade de energia consumida? "))
tipo = input("Qual é o tipo de instalação? ")
if tipo =="residencial":
    if kwh<=500:
        print("O preço por kwh é", 0.40*kwh)
    else:
        print("O preço por kwh é", 0.65*kwh)
elif tipo =="comercial":
    if kwh<=1000:
        print("O preço por kwh é", 0.55*kwh)
    else:
        print("O preço por kwh é", 0.60*kwh)
elif tipo =="industrial":
    if kwh<=5000:
        print("O preço por kwh é", 0.55*kwh)
    else:
        print("O preço por kwh é", 0.60*kwh)

