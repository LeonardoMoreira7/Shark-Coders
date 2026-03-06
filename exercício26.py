from datetime import date
ano_de_nascimento = int(input("Digite o seu ano de nascimento "))
idade = date.today().year - ano_de_nascimento
if idade <18:
    print("Ainda não tens idade para o recenseamento")
elif idade >35:
    print("Já passou o prazo para o recenseamento")
else:
    print("Estás no momento para o recenseamento")