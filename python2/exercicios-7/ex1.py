
def real_dolar(reais):
    return reais/5.20

def dolar_real(dolar):
    return dolar*5.20

opcao = int(input("Qual moeda deseja converter? 1 - Real para Dólar| 2 - Dólar para Real: "))

def menu():
    if opcao == 1:
        reais = int(input("Qual valor deseja converter para dólar? "))
        converter = real_dolar(reais)
        print(f"Total: {converter:.2f} U$")


    elif opcao == 2:
        dolar = float(input("Qual valor deseja converter para reais? "))
        converter = dolar_real(dolar)
        print(f"Total: {converter:.2f} R$")


menu()