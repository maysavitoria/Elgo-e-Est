usuario = 'maysa'
senha = '1514'
 
 #login
  
print('insira o seu nome de usuário e senha')  
usuario2 = input("insira seu nome de usuário: ")
senha2 = input('insira sua senha: ')

if usuario2 == usuario :
    if senha2 == senha:
        print('sucesso! ')
else:
        print ('erro')