import random
import time
computador = random.randint(1, 11)
acertou = False

while not acertou:
    jogador = int(input('QUAL O SEU PALPITE: '))
    if computador == jogador:
        acertou = True
        print('ACERTOU!\n'
              'O VALOR É {}'.format(computador))
    elif computador != jogador:
        acertou = False
        print('TENTE NOVAMENTE')