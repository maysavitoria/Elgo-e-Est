numero1, numero2, operacao=int(input("insira o 1 numero: ")), int(input("insira o 2 numero: ")) , input("insira a operacao: ")
if operacao=="+" or operacao=='adição' or operacao== "mais":
    print(numero1+numero2)
elif operacao=="-" or operacao=='subtração' or operacao== "menos":
    print(numero1-numero2)
elif operacao=="*" or operacao=='multiplicação' or operacao== "vezes":
    print(numero1*numero2)
elif operacao=="/" or operacao=='divisão':
    print(numero1/numero2)
else:
    print("Operacao invalida")
    