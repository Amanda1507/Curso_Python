lisa_num = []
par = []
impar = []

for i in range (20):
    num = int(input("Digite um número: "))
    lisa_num.append (num)
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)