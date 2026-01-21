nome = input("Qual seu nome? ")

turno = input(f"Olá {nome}! Você estuda em qual turno? (Digite: M-matutino ou V-Vespertino ou N- Noturno)")

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa tarte!")
elif turno == "N":
    print("Boa Noite!")
else: 
    print("Horário não identificado!")