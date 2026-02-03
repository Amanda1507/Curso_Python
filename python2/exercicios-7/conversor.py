COTACAO_DOLAR = 5

def dolar_real(qtd_dolares):
    return qtd_dolares * COTACAO_DOLAR

def real_dolar(qtd_reais):
    return qtd_reais / COTACAO_DOLAR


opcao = input("[1] - Conversão de Dolar para Real\n[2] - Conversão Real para Dolar\n[0] - Sair\n")

if opcao == "1":
    dolares = float(input("Digite a quantidade de dólares: "))
    print(dolar_real(dolares))

elif opcao == "2":
    reais = float(input("Digite a quantidade de reais: "))
    print(real_dolar(reais))

elif opcao == "0":
    print("Saindo...")

else:
    print("Opção inválida.")