"""Crie um valor que recebe o nome de um produto, a quantidade que tem no estoque e o
valor unitário do produto. Retorne  o valor total do seu estoque"""
def info(a, b, c):
    total = b * c
    return a, total

mercado = info("fuba", 5, 10)
print(mercado)
