numero = int(input("Escolhe um número "))
divisivel = 0
for i in range(1, numero+1):
    if numero%i ==0:
        divisivel +=1
if divisivel <2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo e foi divisível {divisivel} vezes")