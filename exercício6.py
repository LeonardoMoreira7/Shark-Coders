nota1 = int(input("Qual a primeira nota do aluno?"))
nota2 = int(input("Qual a segunda nota do aluno?"))
media = (nota1+nota2)/2
if media>=60:
    print("Parabéns! Aluno aprovado")
else:
    print("Aluno reprovado")