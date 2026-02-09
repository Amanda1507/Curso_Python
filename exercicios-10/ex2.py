lista_numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista_numeros.append(num)

lista_numeros.sort(reverse = True)

print(lista_numeros)