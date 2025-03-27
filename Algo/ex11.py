email_certo= input('insira um e-mail valido:')
email_certo = str. lower(email_certo)
senha = input(' insira uma senha valida com no minimo 8 caracteres: ')
if len(senha) < 8:
    print("senha muito pequena!")
else: 
    senha_certa=senha
    email= input('insira o e-mail:')
    senha=input("insira a senha:")
    if email == email_certo:
        if senha ==senha_certa:
            print('Bem vindo!')
        else:
            print('e-mail ou senha invalida!') 