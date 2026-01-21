print("Fahrenheit e Ceusius")

print("\n O que quer converter?\n")
opc = int(input("Digite 1 para Celsius e 2 para Fahrenheit: "))

if (opc == 1) :
    f = float(input("Digite a temperatura em Fahrenheit que quer converter para Celsius: "))
    print("A temperatura convertida para Ceelsius é: ",(5*(f-32)/9), "°C")

elif (opc == 2) : 
    c = float(input("Digite a temperatura em Celsius que quer converter para Fahenheit: "))
    print("A temperatura convertida para Fahenheit é: ",((c * 9/5) + 32), "°F")

else: print("Opção inválida!")