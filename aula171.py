lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

soma = [
    (lista_a + lista_b) for lista_a, lista_b in zip(lista_a, lista_b)
]

print(soma)