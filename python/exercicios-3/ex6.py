letra = str(input("Digite um letra: "))

letra = letra.upper()

if letra == ("A" or "E" or "I" or "O" or "U"):
    print(f"A letra digitada: {letra} é vogal")
else:
    print(f"A letra digitada: {letra} é consoante.")