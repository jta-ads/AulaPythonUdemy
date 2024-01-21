from abc import ABC, abstractclassmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractclassmethod
    def sacar(self, valor): ...


    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito {valor}')
    
    def detalhes(self, msg=''):
        print(f'O seu Saldo é {self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >=0:
            self.saldo -= valor
            self.detalhes(f'SAQUE: {valor}')
            return self.saldo
        
        print('Não Possivel sacar o valor desejado')
        self.detalhes(f'Saque Negado: {valor}')
    
  


class ContaCorrente(Conta):
     def __init__(self, agencia, conta, saldo=0, limite=0):
         super().__init__(agencia, conta, saldo)
         self.limite = limite


     def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Saque: {valor}')
            return self.saldo

        print('Não Possivel sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'Saque Negado: {valor}')
    
     def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.conta!r}, {self.agencia!r}, {self.saldo!r}, {self.limite!r}'
        return f'{class_name},  {attrs}'



if __name__ == '__main__':
    cc1 = ContaCorrente(111,222,0,100)
    cc1.sacar(10)
    cc1.sacar(100)
