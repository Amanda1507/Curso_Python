n = int(input("Digite um valor: R$ "))

sobra = n

if sobra >= 100:
    cont = (n // 100)
    sobra = (n % 100)
    print("Você recebera ",cont, " notas de 100")

if sobra >= 50:
    cont = (sobra// 50)
    sobra = (sobra % 50)
    print("Você recebera ",cont ," notas de 50")

if sobra >= 20:
    cont = (sobra // 20)
    sobra = (sobra % 20)
    print("Você recebera ",cont, " notas de 20")

if sobra >= 10:
    cont = (sobra // 10)
    sobra = (sobra % 10)
    print("Você recebera ",cont ," notas de 10")

if sobra >= 5:
    cont = (sobra // 5)
    sobra = (sobra % 5)
    print("Você recebera ",cont ," notas de 5")

if sobra >= 2:
    cont = (sobra // 2)
    sobra = (sobra % 2)
    print("Você recebera ",cont, " notas de 2")

    print("---------------------------------------------")

if sobra < 2:
    print("Não temos maís notas disponiveis\n| O valor devolvido será de: R$",sobra)


#numero = 150
#
#print("Quantas vezes cabe 100 em 150", numero // 100)
#print("O quanto sobrou", numero % 100)
