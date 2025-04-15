numeros=[]
par = []
impar = []
for i in range(8):
    numero= int(input('insira um numero inteiro: '))
    numeros.append(numero)
for numero in numeros:    
    if numero % 2 == 0:
        par.append(numero)
    elif numero % 2 != 0:
        impar.append(numero)
print(par) 
print(impar)       