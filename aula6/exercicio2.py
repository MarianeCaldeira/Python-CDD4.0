"""Crie uma classe chamada Forma, que possui os  atributos area e perímetro.
Implemente as subclasses Retangulo e  Triangulo, que devem conter os métodos calculaArea e calculaPerimetro.
A classe Triangulo deve ter também o atributo altura.
No código de teste crie um objeto da classe Triangulo e outro da classe Retangulo. Verifique se os dois
são mesmo instancias de Forma(use instanceof), e calcule a área de cada um."""

class forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class retangulo(forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self, base, altura):
        print(f'A área do retangulo é {base * altura}')
    def calcularPerimetro(self, base, altura):
        print(f'O perimetro do retangulo é {2 * (base + altura)}')

class triangulo(forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self, base, altura):
        print(f'A área do triangulo é {base * altura}')
    def calcularPerimetro(self, lado1, lado2, lado3):
        print(f'O perimetro do triangulo é {lado1 + lado2 + lado3}')

p1 = triangulo()
p1.calcularArea(2, 2)
p1.calcularPerimetro(2, 2, 2)
p2 = retangulo()
p2.calcularArea(2, 2)
p2.calcularPerimetro(2, 2)

