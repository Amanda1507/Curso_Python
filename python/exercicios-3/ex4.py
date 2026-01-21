nome = input("Qual seu nome? ")
print("Olá ",nome, " vamos calcular seu IMC!")
altura = float(input("Qual sua altura (em metros)? "))
peso = float(input("Digite seu peso (em Kg): "))
imc = peso / (altura * altura)

if imc >= 30:
    print("Cuidado com a saúde!")
else:
    print("Tudo ok!")