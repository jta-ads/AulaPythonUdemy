numero = input('Digite um número inteiro: ')

try:
   numero = int(numero)
   par_impar = numero % 2 == 0
   if par_impar:
        print(f'Número {numero} é PAR')
   else:
        print(f'Número {numero} é ÍMPAR')
except:
     print('Digito Inválido, Por Favor digite número inteiro')