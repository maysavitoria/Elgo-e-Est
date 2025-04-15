nome_produto, quantidade, = input('insira o nome do produto: '), int(input('insira a quantidade que você pegou: '))
valor_unitario= float(input('insira o valor do produto: R$'))
valor_final= valor_unitario * quantidade
if valor_final >= 100:
    print(f"você ganhou 5% de desconto"), print(f'valor da compra: R${valor_final - valor_final*0.5}')
else:
    print(f"valor da compra: R${valor_final}") 