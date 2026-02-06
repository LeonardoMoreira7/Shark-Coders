ordenado = int(input("Qual é o ordenado?"))
if ordenado<500:
    print("O seu novo salário é", ordenado+0.15*ordenado)
elif ordenado>500 and ordenado<1000:
    print("O seu novo salário é", ordenado+0.10*ordenado)
else:
    print("O seu novo salário é", ordenado+0.05*ordenado)