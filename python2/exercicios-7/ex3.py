def somar(a,b):
    return(a + b)

def subtracao(a,b):
    return(a - b)

def multiplicacao(a,b): 
    return(a * b)

def divisao(a,b):
    if opcao == 0:
        print("Erro! Divisão por zero")
    return(a / b)

print("------Calculadora Básica------")

while True:
    print("")
    opcao = int(input("O que deseja calcular? \n0 - Sair\n1 - Adição\n2 - Divisão\n3 - Multiplicação\n4 - Divisão\nOpção: "))
    print("")
    if opcao == 0:
        print("Saindo do programa...")
        break

    if opcao in [1,2,3,4]:
        a = int(input("Digite um valor: "))
        b = int(input("Digite um segundo valor: "))
    

    if opcao == 1:
        print(f"O resultado da soma de {a} + {b} é: {somar(a,b)}")

    elif opcao == 2:
            print(f"O resultado da subtração de {a} - {b} é: {subtracao(a,b)}")

    elif opcao == 3:
        print(f"O resultado da multiplicação de {a} x {b} é: {multiplicacao(a,b)}")

    elif opcao == 4:
        print(f"O resultado da divisão de {a} / {b} é: {divisao(a,b)}")

    else: 
        print("Opção inválida")