def par_ate(n1,n2):
    pares = 0
    if n1 < n2:
        inicio = n1
        fim = n2
    else:
        inicio = n2
        fim = n1
    for i in range(inicio,fim, 1):
        if i%2 == 0:
            print(f"O numero {i} é par.")
            pares += 1

    return(pares)

def menu():
    soma = 0
    opcao = int(input("Digite uma das opções: 1 - Soma| 2 - Verificação de par| 3 - Sair "))

    if opcao == 1:
        qnt = int(input("Quantos números deseja somar? "))

        i = 1
        while i <= qnt:
            num = int(input("Digite um numero: "))
            i += 1

            soma += num

        print(f"A soma dos {qnt} números é: {soma}")

    if opcao == 2:
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero: "))

        total = par_ate(n1,n2)
        print(f"Entre {n1} e {n2}, existem {total} números pares.")

    else:
        print("Tchauuuuu")

menu()