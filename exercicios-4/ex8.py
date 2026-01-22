a = int(input("Digite um valor inicial: "))
b = int(input("Digite um valor final: "))

if a > b:
    inicio = b
    fim = a

else:
    inicio = a
    fim = b


for num in range(inicio, fim + 1):  
    if num > 1: 
        primo = True

        for divisor in range(2, num) : 
            if num % divisor == 0:
                primo = False
                break

        if primo:
            print (num)