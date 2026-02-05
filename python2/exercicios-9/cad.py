lista_nomes= [ ]

opcao = -1
while opcao != "0":
    opcao = input("[1] - Cadastrar Pessoa\n [2] - Remover Pessoa\n [0] - Sair\n Opção: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa que quer cadastrar: ")
        lista_nomes.append(nome)

    elif opcao == "2":
        nome = input("Digite o nome de quem deseja remover: ")
    if opcao != 0:
        lista_nomes.append(opcao)

print("A sua lista de nomes é: ",lista_nomes)