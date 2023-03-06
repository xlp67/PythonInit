list = []
dados = []
maiores = []
menores = []
contador = 0
while True:
    dados.append(input('NOME: '))
    dados.append(int(input('IDADE: ')))
    list.append(dados[:])

    if dados[1] >= 18:
        maiores.append(dados[:])
    else:
        menores.append(dados[:])

    question = input('DESEJA CONTINUAR [S/N]: ').strip().upper()

    if question == 'S':
        dados.clear()
        orgidade = sorted([list[1] for list in list])
        orgnome = [list[0] for list in list]
        print(list)
        print(maiores)
        print(menores)
        print(orgidade)

    if question == 'N':
        break



