list = []
s = list.sort()
follow = 'x'
cont = 0
while True:
    num = int(input('DIGITE UM VALOR: '))
    if num not in list:
        list.append(num)
        cont = cont + 1
        print(list)
        follow = input('DESEJA CONTINUAR [S/N]: ').strip().upper()
        print(list)
    else:
        print('ESSE VALOR JÁ FOI ADICIONADO!')
    if follow == 'N':
        print(f'A LISTA É {list}')
        break
