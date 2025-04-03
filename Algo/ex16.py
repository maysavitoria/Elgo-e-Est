nota1, nota2, nota3 = int(input('insira a 1º nota: ')), int(input('insira a 2º nota: ')), int(input('insira a 3º nota: '))
media = nota1 + nota2 + nota3
media_real= media/3

if media_real >= 7:
    print("aluno aprovado!")
elif media_real >= 5 and media_real < 7:
    print("aluno de recuperação!")  
elif media_real < 5:
    print('reprovado!')
else:
    print("erro!")      