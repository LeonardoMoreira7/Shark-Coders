numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
soma = 0
print(f"Os números que antecedem {numero1, numero2, numero3} são:")
for i in range(numero1, numero2, numero3):
    print(i)
    soma += i
print("A soma é:", soma)