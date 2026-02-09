lista_media = []
soma = 0
divisor = 0
for i in range(4):
    nota = int(input("Digite a nota do aluno: "))
    lista_media.append(nota)
    soma += nota
    divisor += 1
    media = soma / divisor

print(lista_media)
print(f"A média é: {media}")