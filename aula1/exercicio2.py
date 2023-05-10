"""Faça um programa para imprimir os números repetindo em pirâmide de 1 a 5"""
def piramide(num):
    for x in range(1, num):
        print(str(x)*x)
piramide(5)