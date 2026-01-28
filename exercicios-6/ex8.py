
def somar_positivos():
    soma = 0
    positivos = 0
    while True:
        num = int(input("Digite um número. (0 para parar): "))

        if num <= 0:
            break

        if num > 0:
            soma += num
            positivos += 1
            
        else:
            print("Numeros negativos não serão somados.")

    return soma,positivos


res_soma, qtd_positivos = somar_positivos()

print(f"Soma total: {res_soma}")
print(f"Quantidade de números positivos: {qtd_positivos}")