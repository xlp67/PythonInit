lista = []
dados = []
maiores = []
menores = []

while True:
    dados.append(input('DIGITE O NOME: '))
    dados.append((int(input('DIGITE A IDADE: '))))
    lista.append(dados[:])
    pergunta = input('QUER CONTINUAR: [S/N]: ').strip().upper()

    if pergunta == 'S':
        dados.clear()
        continue

    if pergunta == 'N':
        break

for c in lista:
    if c[1] >= 18:
        maiores.append(c[0])
    else:
        menores.append(c[0])

print(lista)
print(maiores)
print(menores)
