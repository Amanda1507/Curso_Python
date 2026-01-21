a = int(input("Digite o valor da variável a: "))
b = int(input("Digite o valor da variável b: "))
c = int(input("Digite o valor da variável c: "))

print("\nComparações: ")
print("\n(a > b) e (c == b) = " , (a > b and c == b))
print("\n(a < b) ou (c > b) = " , (a < b or c > b))
print("\nNÃO (a <> b) = ",not(a != b))