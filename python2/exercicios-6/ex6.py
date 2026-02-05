def par_ate(n1,n2):
    pares = 0
    if n1 < n2:
        inicio = n1
        fim = n2
    else:
        inicio = n2
        fim = n1
    for i in range(inicio,fim, 1):
        if i%2 == 0:
            print(f"O numero {i} é par.")
            pares += 1

    return(pares)
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

total = par_ate(n1,n2)
print(f"Entre {n1} e {n2}, existem {total} números pares.")