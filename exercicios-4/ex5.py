soma = 0
contador = 0

while True:
    num = int(input("Digite um número ( -1 para parar): "))

    if num == (-1):
        break

    soma += num
    contador += 1

if contador > 0:
    media = soma / contador
    print("A média dos números é:", media)
else:
    print("Nenhum número foi digitado.")
