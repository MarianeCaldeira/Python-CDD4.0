import datetime

arquivo = open("extrato.txt", "a")


class ContaBancaria:
    def __init__(self, num_conta, nome_cliente, tipo_conta, status=False):
        self.num_conta = num_conta
        self.saldo = 0
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.limite = 0
        self.extrato = False
        self.data_atual = datetime.datetime.now()
        self.deposito = 0
        self.saque = 0
        self.status = status

    def ativarConta(self, ):
        if self.status == False:
            print(f'A conta foi ativada!')
            self.status = True
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')

    def desativarConta(self, ):
        if self.status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if self.saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessário que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False

    def depositar(self, deposito):
        if self.status:
            if self.limite != 0:
                if self.saldo <= 0:
                    valor_depositado_no_limite = deposito + self.saldo
                    self.saldo = 0
                    valor_depositado_no_saldo = valor_depositado_no_limite + self.saldo
                    self.saldo = valor_depositado_no_saldo
                    print(f"Você depositou R${deposito}")
                    self.extrato = True
                    self.deposito = deposito
                    arquivo.write(
                        f"Número da conta: {self.num_conta}, depósito de R${self.deposito} ocorrido em: {self.data_atual}\n")
                else:
                    self.saldo += deposito
                    print(f"Você depositou R${deposito}")
                    self.extrato = True
                    self.deposito = deposito
                    arquivo.write(
                        f"Número da conta: {self.num_conta}, depósito de R${self.deposito} ocorrido em: {self.data_atual}\n")
            else:
                self.saldo += deposito
                print(f"Você depositou R${deposito}")
                self.extrato = True
                self.deposito = deposito
                arquivo.write(
                    f"Número da conta: {self.num_conta}, depósito de R${self.deposito} ocorrido em: {self.data_atual}\n")
        else:
            print("Você não pode depositar em uma conta inativa!")

    def sacar(self, saque):
        if self.status:
            if self.limite != 0:
                if saque > self.saldo:
                    valor_retirado = saque - self.saldo
                    valor_retirado_do_limite = self.limite - valor_retirado
                    self.saldo = valor_retirado_do_limite - self.limite
                    print(f"você sacou R${saque}")
                    self.extrato = False
                    self.saque = saque
                    arquivo.write(
                        f"Número da conta: {self.num_conta}, saque de R${self.saque} ocorrido em: {self.data_atual}\n")
                else:
                    self.saldo -= saque
                    print(f"você sacou R${saque}")
                    self.extrato = False
                    self.saque = saque
                    arquivo.write(
                        f"Número da conta: {self.num_conta}, saque de R${self.saque} ocorrido em: {self.data_atual}\n")

            elif self.limite == 0 and saque > self.saldo:
                print(f"Você não tem saldo suficiente para esse saque!")


            elif self.limite == 0 and self.saldo > saque:
                self.saldo -= saque
                print(f"você sacou R${saque}")
                self.extrato = False
                self.saque = saque
                arquivo.write(
                    f"Número da conta: {self.num_conta}, saque de R${self.saque} ocorrido em: {self.data_atual}\n")

            elif self.limite == 0 and self.saldo == saque:
                valor_retirado_do_saldo = self.saldo - saque
                valor_sacado_sem_limite = saque - valor_retirado_do_saldo
                self.saldo -= valor_sacado_sem_limite
                print(f"você sacou R${valor_sacado_sem_limite}")
                self.extrato = False
                self.saque = saque
                arquivo.write(
                    f"Número da conta: {self.num_conta}, saque de R${self.saque} ocorrido em: {self.data_atual}\n")
        else:
            print("Você não pode sacar em uma conta desativada!")

    def verificarSaldo(self, ):
        if self.status == True:
            print(f'O saldo da conta é {self.saldo}')
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa!')

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

    def consultarextrato(self):
        if self.status:
            if self.extrato:
                print(
                    f"Número da conta: {self.num_conta}, depósito de R${self.deposito} ocorrido em: {self.data_atual}")
            else:
                print(f"Número da conta: {self.num_conta}, saque de R${self.saque} ocorrido em: {self.data_atual}")
        else:
            print("Não é possível consultar o extrato de uma conta desativada!")


c1 = ContaBancaria(955280, "Mariane", "corrente", False)

# print(conta1.tipo_conta)
c1.ativarConta()
c1.ativarConta()
c1.desativarConta()
c1.ativarConta()
c1.verificarSaldo()
c1.sacar(10)
c1.depositar(50)
c1.verificarSaldo()
c1.sacar(100)
c1.ativarLimite(100)
c1.sacar(100)
c1.sacar(30)
c1.verificarSaldo()
c1.consultarextrato()
