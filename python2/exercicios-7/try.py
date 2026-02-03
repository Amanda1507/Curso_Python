n1 = input("Digite o primeiro número: ")
n2 = input("Digite o primeiro número: ")

try:
    n1 = int(n1)
    n2 = int(n2)

    print(f"A soma dos número é: {n1 + n2}")

except:
    print("Digite um número correto!")