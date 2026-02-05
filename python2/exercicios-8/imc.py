try:
    nome = input("Qual seu nome? ")
    print("Olá ",nome, " vamos calcular seu IMC!")
    altura = float(input("Qual sua altura (em metros)? "))
    peso = float(input("Digite seu peso (em Kg): "))
    imc = peso / (altura * altura)

    print(f"Seu IMC é: {imc:.3f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está com o peso normal.")
    elif imc < 30:
        print("Você está com excesso de peso.")
    elif imc < 40:
        print("Você está obeso.")
    else:
        print("Você está com obesidade extrema.")

except ValueError:
    print("Não aceitamos letras!")

except Exception as erro:
    print("Ocorreu um erro: ",erro)