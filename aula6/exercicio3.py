class atleta():
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso
        self.aquecer = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def aposentar(self):
        def __init__(self):
            super().__init__()
        if self.aposentado == False:
            print("O atleta se aposentou")
            self.aposentado = True
        else:
            print("O atleta ja esta aponsetado!")

    def aquecer(self):
        if self.aposentado == False:
            print("O atleta está aquecendo!")
            self.aquecer = True
        else:
            print("O atleta não pode aquecer pois esta aposentado!")

class corredor(atleta):
    def correr(self):
        if self.aposentado == False:
            print("O atleta começou a correr!")
            self.correndo = True
        else:
            if self.correndo == True:
                print("O atleta ja esta correndo")
            else:
                print("O atleta não pode correr pois está aposentado!")
class nadador(atleta):
    def nadar(self):
        if self.aposentado == False:
            print("O atleta começou a nadar")
            self.nadando = True
        else:
            if self.nadando == True:
                print("O atleta ja está nadando!")
            else:
                print("O atleta não pode nadar pois está aposentado!")

class ciclista(atleta):
    def pelar(self):
        if self.aposentado == False:
            print("O atleta começou a pedalar!")
        else:
            if self.pedalando == True:
                print("O atleta ja está pedalando!")
            else:
                print("O atleta não pode pedalar pois está aposentado!")

class triAtleta(corredor, nadador, ciclista):
