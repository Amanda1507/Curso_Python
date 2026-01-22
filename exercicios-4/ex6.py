n = int(input("Digite o número que deseja saber o fatorial: "))


if n <= 0:
    print("Entrada inválida!")

else:
    fatorial = 1
    for i in range(1, n - 1):
        fatorial *= i

    print(f"O fatorial de {n} é: ",fatorial)
