lista_composta = [["João", 25], ["Maria", 22], ["José", 30], ["Ana", 27]]
idade_desejada = 27
nome = next((x[0] for x in lista_composta if x[1] == idade_desejada), None)
print(nome)