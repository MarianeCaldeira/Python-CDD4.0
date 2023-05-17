def estoque(produto, quantidade, valor):
    total = quantidade * valor
    return produto, total


def some(*num):
    soma = 0
    for x in num:
        soma += x
    return soma


def texto(frase):
    cont = 0
    textoi = ""
    for x in frase:
        if x != " ":
            cont += 1
    print(f"A quantidade de letras na frase é: {cont}")
    for y in range(len(frase) - 1, -1, -1):
        textoi += frase[y]
    print(f"A frase invertida: {textoi}")


def lista(l):
    nova_lista = []
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)


"""-------------------------------------------------------"""


def num(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'não é primo')
                break
        else:
            print(number, 'é primo')
    elif number == 0:
        print(number, 'é zero')
    elif number == 1:
        print(number, 'não é primo')
    else:
        print(number, 'é negativo')


