def tabuada(numero):
    i = 1
    while i <= 10:
        result = numero*i
        print(f"{numero} x {i}: ",result)
        i = i + 1

numero = int(input("Digite um número para ver a tabuada: "))

result = tabuada(numero)
