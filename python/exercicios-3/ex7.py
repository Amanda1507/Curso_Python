nome = str(input("Qual o nome do aluno?"))
n1 = float(input(f"Digite a primeira nota do(a) {nome}"))
n2 = float(input(f"Digite a segunda nota do(a) {nome}"))

media = (n1 + n2)/2

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção")