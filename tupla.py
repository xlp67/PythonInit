import random
from time import sleep
percentual = -3
cont = 0
while True:
    if percentual != 0:
        tupla = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
        a = sorted(tupla)
        b = a[4]
        c = a[5]
        mediana = (b+c)/2
        media = sum(a)/len(a)
        percentual = (mediana-media)/media
        print(mediana)
        print(f'{media}')
        print(f'{percentual}\n')
        cont = cont + 1
    if percentual == 0:
        print(f'\n{cont}')
        break