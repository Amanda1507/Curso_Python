consoantes = []
contador = 0
for i in range (10):
    letras = str(input("Digite uma letra: ")).upper()
    if not in "AEIOU":
        consoantes.append(letras)
        contador += 1
        
print(consoantes)
print(f"Foram digitadas {contador} consoantes.")