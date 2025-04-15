numeros = []

for i in range(0,5):
    numero=int(input('insira um numero inteiro: '))
    numeros.append(numero)
    
maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero > menor:
        menor = numero
        
print(f"o maior numero é {maior}")                