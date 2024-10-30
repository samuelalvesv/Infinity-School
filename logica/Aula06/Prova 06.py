login = "admin"
senha = "123456"

for tentativas in range(2, -1, -1):
    login_digitado = input("Login: ")
    senha_digitada = input("Senha: ")

    if login == login_digitado and senha == senha_digitada:
        print("\nBem vindo!")
        break
    elif tentativas > 0:
        print(f"Login ou senha incorretos, restam {tentativas} tentativas")
    else:
        print("Acesso bloqueado")
