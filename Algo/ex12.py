status_conta= True

valor_saldo=int(input('digite o valor do seu saldo do banco: '))
if valor_saldo >= 0.01:
    print('sua conta continua ativa!')
elif valor_saldo <0 :
    print(' negociar divida')
else:
    print('conta inativa')
    status_conta = False