#coding:utf-8

'''
ENONCE 4 Version: 
Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
Version 1 : utiliser la fonction pow du fichier d’en-tête <math.h> ex : pow(x,n)

'''
from os import system
from math import *

system("cls")
print("\n====================| EXERCICE 4 - VERSION 1 - TD1 |====================\n")
valCorrect = False

# RECUPERATION & CONTROLE DES VALEURS SAISIES
while valCorrect == False:
    try:
        x = float(input("\n--> VEUILLEZ ENTRER UN REEL X: "))
        n = float(input("\n--> VEUILLEZ ENTRER UN REEL N: "))
        valCorrect = True
    except ValueError:
        print("!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
system("pause")

# CALCULS ET AFFICHAGE
print("\n====================>RESULTAT :<====================")
print("\n\t=>",x,"A LA PUISSANCE",n,"EST EGALE A: ",x**n)
print("\n\t=>",x,"A LA PUISSANCE",n,"EST EGALE A: ",pow(x,n))
print("\n\t=>{0} A LA PUISSANCE {1} EST EGALE A: {2}".format(x,n,x**n))
print("\n====================================================\n")
system("pause")