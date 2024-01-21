import json


ARQUIVO = 'pessoa.json'


class Pessoa:
    
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    


p1 = Pessoa('Jota', '30', 'Masc')
p2 = Pessoa('Joao', '15', 'Masc')
p3 = Pessoa('Julia', '15', 'Fem')

bd = [vars(p1), vars(p2), vars(p3)]

def salvar(tarefa, caminho):
    with open (caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefa, arquivo, indent=2, ensure_ascii=False)
    return dados 
  

salvar(bd, ARQUIVO)