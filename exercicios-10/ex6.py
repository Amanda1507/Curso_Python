lista_notas = []
nomes = ["Amanda", "Ana Beatriz", "Davi Dias", "Davi Martins", "Eduarda Navarro", 
         "João Vitor", "Lorena", "Lucas Richard", "Pedro", "Vinicíus"]

for i in range(10):
    print(f"\n--- Lançando notas de: {nomes[i]} ---")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        lista_notas.append(media)

print("\nRelatório de Médias:")
for i in range(10):
    print(f"{nomes[i]}: {lista_notas[i]:.1f}")