valores = []
 
for i in range(4):
    numeros= int(input("insira um numero: "))
    valores.append(numeros)
    
multiplicador = int(input("insira mais 1 numero: "))

print(valores)

valoresatualizado = []

for numeros in valores:
    novo = numeros * multiplicador
    valoresatualizado.append(novo)

print(valoresatualizado)    