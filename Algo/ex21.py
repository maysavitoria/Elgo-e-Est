numeros = []
for i in range(0, 10):
    numero=int(input('insira um número: '))
    numeros.append(numero)

print(numero)

for numero in numeros:
    soma= soma+numero
print(f'a soma dos números é: {soma}')