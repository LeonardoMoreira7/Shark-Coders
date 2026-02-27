def soma():
    resultado = n1 + n2
    print("O resultado da soma é", resultado)
def sub():
    resultado = n1 - n2
    print("O resultado da subtração é", resultado)
def div():
    resultado = n1 / n2
    print("O resultado da divisão é", resultado)
def mult():
    resultado = n1 * n2
    print("O resultado da multiplicação é", resultado)
while True:
    n1 = int(input("Escolhe um número "))
    n2 = int(input("Escolhe outro número "))
    print("0 - Sair\n 1 - Soma\n 2 - Subtrair\n 3 - Dividir\n 4 - Multiplicar\n")
    operacao = int(input("Escolhe a operação "))

    if operacao == 0:
        break
    elif operacao == 1:
        soma()
    elif operacao == 2:
        sub()
    elif operacao == 3:
        div()
    elif operacao == 4:
        mult()