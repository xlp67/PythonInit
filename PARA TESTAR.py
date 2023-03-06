import time
a = int(input('DIGITE O VALOR DE INICIO: '))
b = int(input('DIGITE O INTERVALO: '))

c = a + b
n = 0
quanttermo=1
print(a, end=' ')
time.sleep(1)
while n < 9:
    print(c, end=' ')
    c = c + b
    n = n + 1
    quanttermo = quanttermo + 1
    time.sleep(1)
print(', STOP!', end='')
cont = int(input('\nQUANTOS TERMOS GOSTARIA DE VER A MAIS [0 PARA FINALIZAR]? '))
n = 1
while cont != 0:
    while n < cont+1:
        print(c, end=' ')
        n = n + 1
        c = c + b
        quanttermo = quanttermo + 1
        time.sleep(1)
    cont = int(input('\nQUANTOS TERMOS GOSTARIA DE VER A MAIS [0 PARA FINALIZAR]? '))
    n = 1
print('FORAM INFORMADOS {} TERMOS!'.format(quanttermo))