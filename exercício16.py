numeroi = int(input("Qual é o número inicial? "))
numerof = int(input("Qual é o número final? "))
par = 0
print(f"Os números que estão entre {numeroi, numerof} são:")
for i in range(numeroi, numerof):
    if i%2==0:
        print(i)