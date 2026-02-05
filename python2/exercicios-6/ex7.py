def validar_senha(senha):
        if len(senha) >= 8:
            return(True)
    
        elif len(senha) < 8:
            return(False)
    
def cadastro():
     
    user = input("Digite seu usuário: ")
            
    senha = input("Digite sua senha: ")

    while not validar_senha(senha):
            senha = input("Digite sua senha de 8 digitos ou mais: ")

print("Cadastro realizado com sucesso!")

cadastro()