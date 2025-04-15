notas = []
for i in range(5):
    nota = float(input(f'digite a nota do aluno {i+1}: '))
    notas.append(nota)
    
media = sum(notas)/ len(notas)    
print(f"a média das notas é: {media}")