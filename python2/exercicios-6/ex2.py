def eh_par(numero):
    return(numero%2) == 0


numero = int(input("Digite um numero: "))

result = eh_par(numero)

print(f"Seu número é par. {result}")
    