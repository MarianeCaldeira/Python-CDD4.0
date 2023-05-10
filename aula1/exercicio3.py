"""Faça um programa para imprimir os números sem repetir em pirâmide de 1 a 5"""
def piramide(num):
    for n in range(1, num+1):
        for y in range(1, n+1):
            print(y, end=" ")
        print()
piramide(10)