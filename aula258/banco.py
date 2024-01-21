import conta
import pessoa

class Banco:
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoa.Pessoa] | None = None, 
                 contas: list[conta.Conta] | None = None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
       if conta.agencia  in self.agencias:
           return True
       return False
   
    def _checa_cliente(self, cliente):
       if cliente  in self.clientes:
           return True
       return False
   
    def _checa_conta(self, conta):
       if conta in self.contas:
           return True
       return False
   
    def autenticar(self, cliente, conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)
   

if __name__ == '__main__':
    c1 = pessoa.Cliente('Jota', 30)
    cc1 = conta.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoa.Cliente('Juju', 30)
    cp1 = conta.ContaPoupanca(112, 223, 0)
    c1.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    print(banco.autenticar(c1, cc1))
    print(banco)
