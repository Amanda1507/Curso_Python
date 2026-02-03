try:
    valor = int(input("Digite qual tabuada quer consultar: "))
    
    i = 1

    while i <= 10:
        result = valor * i
        print(f"{valor} x {i} = {result}")
        i += 1 
except ValueError:
    print("Erro: Não aceitamos letras. Por favor, digite um número inteiro.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")