class atleta():
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso
        self.aquecendo = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def aposentar(self):
        if self.aposentado == False:
            print("O atleta se aposentou")
            self.aposentado = True
        else:
            print("O atleta ja esta aposentado!")

    def aquecer(self):
        if self.aposentado == False:
            print("O atleta está aquecendo!")
            self.aquecendo = True
        else:
            self.aquecendo = False
            print("O atleta não pode aquecer pois esta aposentado!")

class corredor(atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def correr(self):
        if self.aposentado == False:
            print("O atleta começou a correr!")
            self.correndo = True
        else:
            if self.correndo == True:
                print("O atleta ja esta correndo")
                self.correndo = True
            else:
                print("O atleta não pode correr pois está aposentado!")
    def pararCorrer(self):
        if self.correndo == True:
            print("O atleta parou de correr!")
            self.correndo = False
        else:
            print("O atleta não estava correndo!")
class nadador(atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def nadar(self):
        if self.aposentado == False:
            print("O atleta começou a nadar")
            self.nadando = True
        else:
            if self.nadando == True:
                print("O atleta ja está nadando!")
                self.nadando = True
            else:
                print("O atleta não pode nadar pois está aposentado!")
    def pararNadar(self):
        if self.nadando == True:
            print("O atleta parou de nadar!")
            self.nadando = False
        else:
            print("O atleta não estava nadando!")


class ciclista(atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def pedalar(self):
        if self.aposentado == False:
            print("O atleta começou a pedalar!")
            self.pedalando = True
        else:
            if self.pedalando == True:
                print("O atleta ja está pedalando!")
                self.pedalando = True
            else:
                print("O atleta não pode pedalar pois está aposentado!")
    def pararPedalar(self):
        if self.pedalando == True:
            print("O atleta parou de pedalar!")
            self.pedalando = False
        else:
            print("O atleta não estava pedalando!")

class triAtleta(corredor, ciclista, nadador):
    def __init__(self, peso):
        super().__init__(peso)
    def correr(self):
        if self.nadando == True:
            print("O atleta não pode correr pois está nadando!")
        elif self.pedalando == True:
            print("O atleta não pode correr pois está pedalando!")
        elif self.correndo == True:
            print("O atleta ja está correndo!")
        else:
             print("O atleta começou a correr")
             self.correndo = True

    def nadar(self):
        if self.correndo == True:
            print("O atleta não pode nadar pois está correndo!")
        elif self.pedalando == True:
            print("O atleta não pode nadar pois está pedalando!")
        elif self.nadando == True:
            print("O atleta ja está nadando!")
        else:
            print("O atleta começou a nadar!")
            self.nadando = True

    def pedalar(self):
        if self.correndo == True:
            print("O atleta não pode pedalar pois está correndo!")
        elif self.nadando == True:
            print("O atleta não pode pedalar pois está nadando!")
        elif self.pedalando == True:
            print("O atleta ja está pedalando!")
        else:
            print("O atleta começou a pedalar!")
            self.pedalando = True

p1 = corredor(50)
p1.aquecer()
p1.correr()
p1.pararCorrer()

p2 = nadador(50)
p2.aquecer()
p2.nadar()
p2.pararNadar()

p3 = ciclista(50)
p3.aquecer()
p3.pedalar()
p3.pararPedalar()

p4 = triAtleta(60)
p4.correr()
p4.correr()
p4.nadar()
p4.correr()
p4.pararCorrer()
p4.nadar()
p4.pararNadar()
p4.pedalar()
p4.pararPedalar()
p4.aquecer()
p4.pedalar()
