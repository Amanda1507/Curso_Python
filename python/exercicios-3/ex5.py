sexo = str(input("Qual o seu sexo? (Digite F ou M) "))

sexo = sexo.upper()
if sexo == "F":
    print("F - Feminino")

elif sexo == "M":
    print("M - Masculino")
    
else: 
    print("Sexo inválido")