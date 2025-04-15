tabuada = []

numero = int(input("insira um numero inteiro: "))
i = 0
for vezes in range(0, 10):
    i = i + 1
    mult = numero * i
    tabuada.append(mult)
print(tabuada)
