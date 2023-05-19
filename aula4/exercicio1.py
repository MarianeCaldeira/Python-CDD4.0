class Pessoa:

    def __init__(self, nome, peso, idade, comendo=False, falando=False, andando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andando

    def comer(self, comida):
        self.comida = comida
        if self.comendo == True:
            print(f"{self.nome} ja esta comendo!")
        else:
            if self.falando == True:
                print(f'{self.nome} não pode comer pois está falando!')
            else:
                print(f'{self.nome} foi comer {self.comida}!')
                self.comendo = True

    def pararDeComer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer!')
            self.comendo = False
        else:
            print(f'{self.nome} não parou de comer pois não estava comendo!')

    def falar(self):
        if self.falando == True:
            print(f'{self.nome} ja estava falando!')
        else:
            if self.comendo == True:
                print(f'{self.nome} não pode falar pois esta comendo')
            else:
                print(f'{self.nome} começou a falar!')
                self.falando = True

    def pararDeFalar(self):
        if self.falando == True:
            print(f'{self.nome}, cale a boca!')
        else:
            print(f'{self.nome} não está falando!')

    def andar(self):
        if self.andando == True:
            print(f'{self.nome} ja está andando!')
        else:
            print(f'{self.nome} começou a andar!')
            self.andando = True


p2 = Pessoa("Maria", 54, 19)
p2.comer("maçã")
p2.comer("maçã")
p2.pararDeComer()
p2.pararDeComer()
p2.falar()
p2.comer("maça")
p2.andar()
p2.andar()
