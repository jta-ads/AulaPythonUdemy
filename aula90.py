import os

lista = []

while True:
    print('Selecione uma opção')
    dados = input('[i]inserir [a]pagar [l]istar ').lower()

    if len(dados) > 1:
        os.system('cls')
        print('Digito invalido!')
        continue

    if dados == 'i':
       os.system('cls')
       valor = input('Valor: ') 
       lista.append(valor)
     

    if dados == 'a':
        try:
            apagar = input('Qual Indice Deseja Apagar: ')
            apagar = int(apagar)
            del lista[apagar]
        except:
            print('Lista está Vazia!')

    if dados == 'l':
        if len(lista) != 0:
            for indice, item in enumerate(lista):
                os.system('cls')
                print(indice, item)
        else:
            os.system('cls')
            print('Lista vazia, Digite algum item!')

