import random
palpites=[]
sorteado = random.randint(1,20)

while True:
    palpite = int(input(' digite seu palpite: '))
    palpites.append(palpite)
    if palpite == sorteado:
        print ('parabéns você acertou!')
        break