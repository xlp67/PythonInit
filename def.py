lista = [1, 2, 3]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = 2*lst[pos]
        pos = pos + 1
    print(lista)


dobra(lista)

