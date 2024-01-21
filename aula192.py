

apagado = None
lista = []
while True:
   
    for i in lista:
        print(i)
    print()

    print('Escolha [Listar][Desfazer][Refazer]')
    caminho = input('Escolha um Caminho: ')

    if caminho.lower() == 'listar':
        if len(lista) == 0:
            print('Nada para Listar')
            continue
        for i in lista:
            print(i)
        print()

    elif caminho.lower() == 'desfazer':
        if len(lista)== 0:
            print('Nada para desfazer')
            continue
        apagado = lista.pop()
    elif caminho.lower() == 'refazer':
        if apagado is None:
            print()
            print('Nada para Refazer')
            print()
            continue
        lista.append(apagado)
        apagado = None
    else:
        lista.append(caminho)
    print()
    print('TAREFAS: ')