consoantes = []
contador = 0

for i in range(10):
    letra = input(f"Digite a {i+1}ª letra: ").upper()
    
    if letra.isalpha() and letra not in "AEIOU":
        consoantes.append(letra)
        contador += 1
        
print("-" * 20)
print(f"Consoantes encontradas: {consoantes}")
print(f"Total de consoantes: {contador}")