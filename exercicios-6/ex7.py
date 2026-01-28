def validar_senha(senha):
    if len(senha) >= 8:
        return("Senha valida")
    
    elif len(senha) < 8:
        return("Senha inválida. Crie outra")
    
user = input("Digite seu usuário: ")
        
senha = input("Digite sua senha: ")

valido = validar_senha(senha)

print("Sua senha uma",valido)