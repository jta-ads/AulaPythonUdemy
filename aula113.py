
def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

def par_impar(x):
    if x % 2 == 0:
        retorno = 'Par'
    else:
        retorno = 'Impar'
    return retorno

result = multiplica(3,1,3,1)

print(result)

result_2 = par_impar(result)

print(result_2)