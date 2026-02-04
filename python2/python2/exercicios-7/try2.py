try:
    valor1 = float(input("Digite um número: "))
    print(5/valor1)

except ZeroDivisionError:
    print("Não é possivel dividir um número por zero,")

except Exception as erro:
    print("Ocorreu um erro:",erro)