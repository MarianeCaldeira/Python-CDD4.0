"""Faça uma função que conte quantas vogais tem no texto:
O rato roeu a roupa do rei de Roma"""

def vogais(text):
    cont = 0
    for x in text:
        if x in "aeiouAEIOU":
            cont += 1
    print("A quantidade de vogais no texto é:", cont)
texto = "O rato roeu a roupa do rei de Roma"
print(texto)
vogais(texto)
