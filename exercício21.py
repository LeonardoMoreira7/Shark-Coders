frase = (input("Escolhe uma frase"))
letra = (input("Escolhe uma letra"))
soma = 0
if letra in frase:
    print(f"A letra {letra} aparece na frase")
for i in frase:
    if i == letra:
        soma += 1
print(f"A letra {letra} aparece {soma} vezes na frase")