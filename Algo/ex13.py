nome, idade, turma = input('insira seu nome completo: '), int(input('insira sua idade: ')), input('insira sua turma: ') 
if idade >= 6:
    print(f'Aluno cadastrado com socesso: {nome}, {idade}, {turma}')
else:
    print("matricula negada!")    