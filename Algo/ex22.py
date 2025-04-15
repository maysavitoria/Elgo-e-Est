palavras = []
total = 0
for i in range(0, 5):
    palavra = input("insira uma palavra: ")
    palavras.append(palavra)

for palavra in palavras:
    caracteres = len(palavra)
    if caracteres > 5:
        total = total + 1
print(f'o total de palavras com mais de 5 caracteres é: {total}')