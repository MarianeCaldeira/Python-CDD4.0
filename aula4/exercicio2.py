class Conta:

    def __init__(self, conta, saldo, nomeCliente, tipo, status=True):
        self.nomeCliente = nomeCliente
        self.conta = conta
        self.saldo = saldo
        self.status = status
        self.tipo = tipo

    def depositar(self, ):
        if self.status == True:
            print(f"O dinheiro foi depositado!")
            self.status = True
        else:
            print(f'O dinheiro não foi depositado pois a conta está inativa')
            self.status = False

    def sacar(self, saldo):
        self.saldo = saldo
        if self.status == False:
            print(f"Não foi possível sacar o dinheiro pois a conta está inativa!")
            self.status = False
        else:
            if self.saldo == 0:
                print(f"Não foi possível sacar o dinheiro pois a conta não tem saldo!")
            else:
                print(f'O dinheiro foi sacado com sucesso')
                self.status = True

    def verificarSaldo(self, saldo):
        self.saldo = saldo
        if self.status == True:
            print(f'O saldo da conta é {self.saldo}')
            self.status = True
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa')
            self.status = False

    def ativar(self, status):
        if status == False:
            print(f'A conta foi ativada!')
            self.status = True
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')
            self.status = True

    def desativar(self, saldo, status):
        self.saldo = saldo
        if status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessario que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False

p2 = Conta(955280, 1000, "Mariane", "DACC")
p2.desativar(1, status=True)
p2.desativar(1, status=False)
p2.desativar(0, status=True)
p2.depositar()
p2.ativar(status=True)
p2.ativar(status=False)
p2.depositar()
p2.sacar(1)
p2.sacar(0)
p2.desativar(0, status=True)
p2.sacar(1)
p2.verificarSaldo(100)
p2.ativar(status=False)
p2.verificarSaldo(100)
p2.desativar(0, status=True)

