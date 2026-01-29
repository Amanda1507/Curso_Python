def cambio():
    valor = float(input("Qual valor deseja converter? "))

    opcao = int(input(f"Qual moeda você Tem agora? \n 1 - Reais \n 2 - Dólar \n 3 - Libra \n Opção: "))

    if opcao == 1:
        opn = int(input(f"Para qual moeda quer converter os {valor} R$? 1 - Dólar| 2 - Libra "))
        if opn == 1:
            print (f"O valor convertido é: {valor/5.20:.2f} R$")
        
        else:
            print (f"O valor convertido é: {valor/7.16:.2f} R$")
        
    elif opcao == 2:
        opnn = int(input(f"Para qual moeda quer converter os {valor} U$? 1 - Real| 2 - Libra "))
        if opnn == 1:
            print (f"O valor convertido é: {valor/5.20:.2f} U$")
        
        else: 
            print (f"O valor convertido é: {valor*1.25:.2f} U$")
        
    elif opcao == 3:
        opnnn = int(input(F"Para qual moeda quer converter as {valor}C? 1- Real| 2 - Dólar "))
        if opnnn == 1:
            print (f"O valor convertido é: {valor/7.16:.2f} C")
        
        else:
            print (f"O valor convertido é: {valor*1.25:.2f} C")
        
    else:
        print("Opção inválida")
        


cambio()