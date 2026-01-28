def eh_par(numero):
    if (numero%2) == 0:
        return (True)

    else:
        return(False)

numero = int(input("Digite um numero: "))

result = eh_par(numero)

print(f"Seu número é par. {result}")
    