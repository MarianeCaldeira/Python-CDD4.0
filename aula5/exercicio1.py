class animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def come(self):
        print(f'o {self.nome} foi come...')
    def emitirSom(self):
        print(f'o {self.nome} está emitindo som...')

class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'o {self.nome} está miando...')

class cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'o {self.nome} está latindo...')

class vaca(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

p2 = vaca("Black", "Preta")
p2.emitirSom()
