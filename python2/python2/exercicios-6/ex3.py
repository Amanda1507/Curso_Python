def calc_media(n1,n2,n3):
    return((n1 + n2 + n3)/3)

n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
n3 = int(input("Digite a terceira nota:"))

result = calc_media(n1,n2,n3)
    
if result >= 7:
    print(f"A média é: {result}")
else:
    print("Você não passou.")
