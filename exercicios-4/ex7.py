
quantidade = int(input("Quantos números deseja digitar? "))

num = int(input("Digite um número: "))
menor = num
maior = num

for i in range(quantidade - 1):
    num = int(input("Digite um número: "))

    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior número:", maior)
print("Menor número:", menor)