dados = {}
lista = []

while True:
    dados['nome'] = str(input('NOME: '))
    dados['idade'] = int(input('IDADE: '))
    lista.append(dados.copy())
    dados.clear()
    print(len(lista))

    while True:
        pergunta = str(input('QUER CONTINUAR [S/N]: ').strip().upper())
        if pergunta in 'SN':
            break
        print('DIGITE APENAS S OU N')

    if pergunta == 'S':
        for c in lista:
            if c['idade'] >= 18:
                print(c['nome'], ' É MAIOR DE IDADE!')
        continue

    if pergunta == 'N':
        break
