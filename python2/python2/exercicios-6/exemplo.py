def somar():
    #Como a função não recebe parametros, é necessário pegar os valores
    valor_1 = int(input("Digite o primeiro valor: "))
    valor_2 = int(input("Digite o segundo valor: "))
    return(valor_1 + valor_2)
    #Função sem retorno, só mostra o resultado usando a função print.

resultado = somar()
print("O resultado da soma é: ",resultado)