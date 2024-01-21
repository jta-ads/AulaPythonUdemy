import copy


produtos = [
    {'nome': 'Produto 5', 'preco':10.00},
    {'nome': 'Produto 1', 'preco':22.32},
    {'nome': 'Produto 3', 'preco':10.11},
    {'nome': 'Produto 2', 'preco':105.87},
    {'nome': 'Produto 4', 'preco':69.90},
]
novo_produtos = copy.deepcopy(produtos)
cont = 0
for valor in produtos:
    preco = valor.get('preco')
    preco = preco * 0.10 + preco
    novo_produtos[cont]['preco'] = round(preco, 2)
    cont +=1

ordem_maior = sorted(novo_produtos, key= lambda obj: obj['preco'], reverse=True)
for ordem_maior in ordem_maior:
    print(ordem_maior)

ordem_menor = copy.deepcopy(novo_produtos)
ordem_menor = sorted(ordem_menor, key= lambda obj:obj['preco'], reverse=False)
print()
for ordem_menor in ordem_menor:
    print(ordem_menor)