valor = float(input('insira  valor da compra: '))
if valor > 60 and valor <120:
    print('desconto de 5%'), print(f'valor final:{valor-valor*5/100}')
elif valor  > 120 and valor < 400:
    print('desconto de 20%'), print(f'valor final:{valor-valor*20/100}') 
elif valor > 400:
    print('desconto de 50%'), print(f'valor final:{valor-valor*50/100}')  
else: 
    print('sem desconto'), print(f'valor final:{valor}')         