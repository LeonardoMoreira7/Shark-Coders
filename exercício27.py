from time import sleep
valor = int(input("Insere um valor "))
while True:
    valor -= 1
    print(valor)
    sleep(1)
    if valor == 0:
        break