import re
import sys
import random


digito_gerado = ''
for item in range(9):
    entrada = random.randint(0, 9)
    entrada = str(entrada)
    digito_gerado += entrada



cpf = re.sub(r'[^0-9]', '', digito_gerado)

digito_repetidos = digito_gerado == digito_gerado[0]*len(digito_gerado)

if digito_repetidos:
    print('Digitos Repetidos!')
    sys.exit()

digito9 = cpf[:9]


count = 10
soma9 = 0
for i in digito9:
    i = int(i)
    soma9+=i*count
    count -= 1

result_1 = soma9 * 10 % 11
resto9 = result_1 if result_1 <= 9 else 0



digito10 = digito9 + str(resto9)


count = 11
soma10 = 0
for i in digito10:
    i = int(i)
    soma10+=i*count
    count -= 1


result_2 = soma10 * 10 % 11 
resto10 = result_2 if result_2 <= 9 else 0 

cpf_gerado = f'{digito9}{resto9}{resto10}'

print(cpf_gerado)






