#coding: utf-8

'''
ENONCE 17 : Faire un programme qui calcule le PGCD de deux nombres saisis au clavier en utilisant l'astuce
suivante: soustrait le plus petit des deux entiers du plus grand jusqu'à ce qu'ils soient égaux.

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 17 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        a = int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: "))
        b = int(input("-> VEUILLEZ SAISIR UN DEUXIEME NOMBRE ENTIER: "))
        # assert b != 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

# CALCULS
while a != b:
    if a > b:
        a = a - b
    else:
        if a < b:
            b = b - a

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t\tLE PGCD DE CES DE CES DEUX NOMBRES EST: {0}\n".format(a))
print("\n==========================================================================\n")
os.system("pause")
    