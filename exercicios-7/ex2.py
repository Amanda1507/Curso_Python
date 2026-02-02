def cambio():
    while True:
        print("\n--- Conversor de Moedas ---")
        opcao = int(input("Qual moeda você TEM agora?\n0 - Sair\n1 - Reais\n2 - Dólar\n3 - Libra\nOpção: "))

        if opcao == 0:
            print("Saindo do programa...")
            break
        
        if opcao not in [1, 2, 3]:
            print("Opção inválida! Tente novamente.")
            continue

        valor = float(input("Qual valor deseja converter?"))

        if opcao == 1:
            opn = int(input(f"Para qual moeda quer converter os {valor} R$? 1 - Dólar| 2 - Libra "))
            if opn == 1:
                print (f"O valor convertido é: {valor/5.20:.2f} R$")
            
            else:
                print (f"O valor convertido é: {valor/7.16:.2f} R$")
            
        elif opcao == 2:
            opnn = int(input(f"Para qual moeda quer converter os {valor} U$? 1 - Real| 2 - Libra "))
            if opnn == 1:
                print (f"O valor convertido é: {valor*5.20:.2f} $")
            
            else: 
                print (f"O valor convertido é: {valor*0.78:.2f} $")
            
        elif opcao == 3:
            opnnn = int(input(F"Para qual moeda quer converter as {valor}C? 1- Real| 2 - Dólar "))
            if opnnn == 1:
                print (f"O valor convertido é: {valor*7.16:.2f} £")
            
            else:
                print (f"O valor convertido é: {valor*1.25:.2f} £")
            
        else:
            print("Opção inválida")


            


cambio()