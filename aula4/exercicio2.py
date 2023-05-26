class Conta:

    def __init__(self, conta, nomeCliente, tipo):
        self.nomeCliente = nomeCliente
        self.conta = conta
        self.saldo = 0
        self.status = False
        self.limite = 0
        self.tipo = tipo
        self.limiteUsado = 0

    def depositar(self, valord):
        if self.status == True:
            print(f"O dinheiro foi depositado!")
            self.saldo = valord
            if self.limiteUsado > 0:
                print("O dinheiro foi depositado e descontado na sua divida de limite!")
                self.saldo = self.saldo - self.limiteUsado
                self.limiteUsado = self.limiteUsado - self.saldo

        else:
            print(f'O dinheiro não foi depositado pois a conta está inativa!')

    def sacar(self, valorS):
        if self.status == False:
            print(f"Não foi possível sacar o dinheiro pois a conta está inativa!")
        else:
            if valorS < self.saldo:
                print(f'O dinheiro foi sacado com sucesso!')
                self.saldo = self.saldo - valorS
            else:
                calculo = valorS - self.saldo
                self.limiteUsado = self.limiteUsado + calculo
                self.saldo = 0
                print(f"O dinheiro foi sacado com sucesso!")

    def verificarSaldo(self, ):
        if self.status == True:
            print(f'O saldo da conta é {self.saldo} e o saldo usado é {self.limiteUsado}!')
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa!')

    def ativar(self, ):
        if self.status == False:
            print(f'A conta foi ativada!')
            self.status = True
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')

    def desativar(self, ):
        if self.status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if self.saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessario que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False

    def ativarLimite(self, valorL):
        if self.status == True:
            print(f"Limite ativado, seu limite é {valorL}!")
            self.limite = valorL
        else:
            print("Limite não pode ser ativado pois a conta não está ativa!")

    def desativarLimite(self):
        if self.limite > 0:
            print(f'Seu limite foi desativado!')
            self.limite = 0
        else:
            print(f'Você não tem limite ativo!')

p2 = Conta(955280, "Mariane", "DACC")
p2.ativar()
p2.ativarLimite(10)
p2.verificarSaldo()
p2.depositar(100)
p2.verificarSaldo()
p2.sacar(110)
p2.verificarSaldo()
p2.depositar(20)
p2.verificarSaldo()
p2.sacar(10)
