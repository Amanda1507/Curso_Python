opn = int(input("O que quer converter? (1 = metros | 2 = centimetros) "))

if opn == 1:
    metros = float(input("Digite o valor que quer converter para centimetros: "))
    print(metros * 100)

elif opn == 2:
    cent = float(input("Digite o valor que quer converter para metros: "))
    print(cent / 100)

else:
    print("Opção inválida!")
