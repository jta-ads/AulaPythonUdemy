import os
palavra = 'dado'

count = 0

letra_digitada = ''
letras_acertadas = ''
while True:

    letra_digitada = input('\nDigite uma letra: ')

    if len(letra_digitada) > 1 :
        print('Digite apenas um letra!')
        continue
    
    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    else:
        count +=1
    palavra_formatada = ''
    for i in palavra:
        if i in letras_acertadas:
            palavra_formatada += i
            #print(f'{i}', end="")
        else:
            palavra_formatada += '*'
            #print('*', end="") 
    print(palavra_formatada)
        
    if palavra_formatada == palavra:
        os.system('cls')
        print('PARABÉNS')
        print(f'Você acertou a palavra "{palavra_formatada}"')
        print(f'FORAM {count} TENTATIVAS')
       
  
    
