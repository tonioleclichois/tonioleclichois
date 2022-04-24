#!/usr/bin/env python
# -*- coding: cp1252 -*-

car = [' ', ',', ':', ';', '.', "'", '-', '!', '?', "’", "\n"]


def freq(texte):
    d, compteur = {}, 0
    for c in texte:
        if c not in d:
            if c not in car:
                d[c] = 1
                compteur += 1
        else:
            d[c] += 1
            compteur += 1
    L = sorted(d.items(), key=lambda colonne: colonne[1], reverse=True)
    for i in L:
        print('{} : {}'.format(i[0], round(i[1] / compteur*100, 1)))
    return d, compteur, len(L)


file = 'txt_crypt'
code = open(file, 'r').readlines()

clef = {"A": "c", "B": "i", "C": "o", "D": "v", "E": "y", "F": "b", "G":"l", "H":"H", "I":"f", "J":"t", "K":"q", "L":"m", "M":"a", "N":"d", "O":"O", "P":"h", "Q":"p", "R":"s", "S":"j", "T":"n", "U":"u", "V":"r", "W":"g", "X":"e", "Y":"Y", "Z":"x"}

txt = ""

for letter in code[0]:
    if letter in clef.keys():
        txt += clef[letter]
    else:
        txt += letter

print(code, "\n\n\n", txt)
