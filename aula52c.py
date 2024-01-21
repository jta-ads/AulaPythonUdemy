primeiro_nome = input('Digite seu primeiro nome: ')

nome_curto = len(primeiro_nome) <= 4
nome_normal = len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6
nome_grande = len(primeiro_nome) > 6 

if nome_curto:
    print('Seu nome é curto')
if nome_normal:
    print('Seu nome é normal')
if nome_grande:
    print('seu nome é grande')

