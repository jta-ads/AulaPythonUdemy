import json
from aula206_a import ARQUIVO



def ler(caminho):
    with open(caminho, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    return dados

print(ler(ARQUIVO))