print("Bem-vindo(a) a sua calculadora digital!")
def somar(a, b):
    soma = a + b
    print(a, "+", b, "=", soma)
def subtrair(a, b):
    subtracao = a - b
    print(a, "-", b, "=", subtracao)
def multiplicar(a, b):
    multiplicacao = a * b
    print(a, "*", b, "=", multiplicacao)
def dividir(a, b):
    divisao = a / b
    print(a, "/", b, "=", divisao)

while True:
    print("Escolha uma das opções:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    escolha = int(input("Qual ação você deseja realizar? "))
    if escolha == 1:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))
        somar(n1, n2)
    elif escolha == 2:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))
        subtrair(n1, n2)
    elif escolha == 3:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))
        multiplicar(n1, n2)
    elif escolha == 4:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))
        dividir(n1, n2)
    elif escolha == 5:
        print("Programa encerrado!")
        break
    else:
        print("Informe um número de acordo com as opções do menu!")
