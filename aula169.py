capital = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

unir =[
    (capital, estado) for capital, estado in zip(capital, estado)
]


print(unir)