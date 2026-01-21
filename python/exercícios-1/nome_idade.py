ano = int(input("Em qual ano estamos? "))
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
inicio = int(input("Estamos no inicio do ano? (1 = sim e 2 = não) "))

if (inicio == 1 ) : print(nome," possui ",idade, " anos de idade e nesceu em ",(ano - 1 - idade))
else : print(nome," possui ",idade, " anos de idade e nasceu em ",(ano - idade))
