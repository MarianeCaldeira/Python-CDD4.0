"""Crie uma classe chamada Ingresso. que possui um valor em reais e um método imprimeValor()
Crie uma classe VIP, que herda de Ingresso e possui um valor adicional. Crie um método que
retorne o valor do ingresso VIP (com o adicional incluído)."""

class ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print(f'Valor do ingresso: R${self.valor}')

class vip(ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprimeValor(self, adicional):
        print(f'Ingresso VIP: R${(self.valor * adicional / 100) + self.valor}')

p1 = ingresso(50)
p1.imprimeValor()
p2 = vip(50)
p2.imprimeValor(50)
