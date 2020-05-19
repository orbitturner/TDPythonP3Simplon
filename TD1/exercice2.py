#coding:utf-8

'''
ENONCE 2: 
Ecrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle et lui retourne sa surface et son
périmètre.
PI = 4 * arc tangente de 1. la fonction arc tangente est atan ex : atan(2).
// Aire = Pi*r2 | Perimetre = 2*Pi*r
'''
import os
from math import *

PI = 4 * atan(1)
ray = 0
os.system("cls")
print("\n====================| EXERCICE 2 - TD1 - AIR_PER |====================\n")

# RECUPERATION ET CONTROLE DE LA SAISIE
while ray <= 0:
    try:
        ray = int(input("\n==> VEUILLEZ DONNER LE RAYON DU CERCLE : \n"))
        error = False
    except:
        ray = -1
        error = True
        print(" !! ENTREZ UN NOMBRE ENTIER VALIDE !!")
        os.system("pause")
        os.system("cls")
        continue
    finally:
        if ray <= 0 and error == False :
            print("!! LE NOMBRE DOIT ETRE STRICTEMENT SUPERIEUR A ZERO")
            os.system("pause")
            os.system("cls")

# CALCULS ET AFFICHAGE
print("\n→ Le PERIMETRE de votre cercle est {0}".format(PI*(ray**2)))
print("\n→ La SURFACE de votre cercle est", 2*PI*ray)
print("=================================================================================")
os.system("pause")
os.system("exit")