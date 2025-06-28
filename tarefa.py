#2.prograna que pedira um cadastro 
while True:
    try:
        nome_usuario = input("Digite sue nome de usuario:")
        senha_usuario = input("Dgiete sua senha:")
        if nome_usuario  == senha_usuario:
           raise ValueError("A senha não pode ser igual ao nome.")
        print("Escrisão com sucesso")
        break
    except ValueError as erro:
        print(f"Erro:{erro}\ntente novamente.\n")