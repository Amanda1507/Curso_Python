nome = str(input("Digite o nome do aluno: "))
n1 = float(input(f"Digite a primeira nota do(a) {nome}: "))
n2 = float(input(f"Digite a segunda nota do(a) {nome}: "))
n3 = float(input(f"Digite a terceira nota do(a) {nome}: "))

media = (n1+n2+n2)/3

if media >= 7:
    print(f"{nome} está aprovado(a)!")
elif media > 4:
    print(f"{nome} está em recuperação!")
else:
    print(f"{nome} está reprovado(a)!")