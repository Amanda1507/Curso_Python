nome = input("Qual é o seu nome? ")
idade = input("Qual sua idade? ")
carteira = int(input("Possui carteira de motorista? 1-Sim | 2-Não"))

if idade >= 18:
    if carteira == 1:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")

else: 
    print("Menor de idade!")