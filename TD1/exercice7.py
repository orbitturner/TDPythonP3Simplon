#coding: utf-8

'''
ENONCE 7 : Décomposition d’un montant en euros Écrire un algorithme permettant de décomposer un montant
entré au clavier en billets de 20, 10, 5 euros et pièces de 2, 1 euros, de façon à minimiser le nombre de billets et de
pièces.

'''
import os
from math import *

os.system("cls")
print("\n====================| EXERCICE 7 - TD1 |====================\n")

valCorrect = False
# generalError = "\n!! LA SOMME DOIT ETRE STRICTEMENT > 0 !!"

# RECUPERATION & CONTROLE DES VALEURS SAISIES
while valCorrect == False:
    try:
        somme = int(input("\n--> Veuillez entrez une somme à décomposer : "))
        assert somme > 0
        valCorrect = True
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n!! LA SOMME DOIT ETRE STRICTEMENT > 0 !!")
        continue
os.system("pause")

# CALCULS
b100 = somme // 100
reste = somme % 100

b50 = reste // 50
reste = reste % 50

b10 = reste // 10
reste = reste % 10

p2 = reste // 2
reste = reste % 2

# AFFICHAGES
print("\n===============================>RESULTAT :<===============================\n")
print("==> {:4d} billet(s) de 100 euros".format(b100))
print("==> {:4d} billet(s) de 50 euros".format(b50))
print("==> {:4d} billet(s) de 10 euros".format(b10))
print("==> {:4d} pieces(s) de 2 euros".format(p2))
print("==> {:4d} pieces(s) de 1 euro".format(reste))
print("\n==========================================================================\n")
