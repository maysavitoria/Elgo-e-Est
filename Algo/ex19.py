idade=int(input('insira a sua idade: '))
genero = input('feminino ou masculino? (F ou M)')
categoria = input(" você é atleta? (sim ou não)")

genero = genero.upper()
categoria = categoria.upper()

if idade < 15:
    print("artigos infantís")
elif idade >= 15 and idade <= 21 and genero == "F":
    print("maquiagem e moda")
elif idade >= 15 and idade <= 32 and genero == "M" and categoria == "SIM":
    print("artigos esportivos")
elif idade >= 15 and idade <= 21 and genero == "M" and categoria == "NÃO":
    print('videogames')
elif idade >= 21 and idade <= 32 and genero == "M" and categoria == "NÃO":
    print('livros, jardinagem e eletrodomésticos')
elif idade >= 22 and idade <= 35 and genero == "F" and categoria == "SIM":
    print('artigos esportivos e itens de casa') 
else:
    print('erro')                  