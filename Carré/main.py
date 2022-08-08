#!/usr/bin/env python3

name = input('Bonjour, veuillez entrer votre nom : ')
 
print('Bonjour '+ name)

n = int(input('Entrez un nombre, et son carré sera affichée : '))

if n < 0 :
    raise ValueError('Vous devez saisir un nombre positif')

square = n *n

print(square)