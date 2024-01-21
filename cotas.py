from random import sample


lista_aleatorias =[701, 702, 703, 704, 705, 707, 708, 709, 711, 713, 715, 716, 720, 721, 722, 725, 728, 729, 730]
cotas_aleatórias = sample(lista_aleatorias, 5)



nova_cota = []
for cotas in cotas_aleatórias:
    nova_cota.append(cotas)
    lista_aleatorias.remove(cotas)

nova_cota = sorted(nova_cota)

print(nova_cota)
print(lista_aleatorias)
 