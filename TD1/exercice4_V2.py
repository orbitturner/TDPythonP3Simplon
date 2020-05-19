#coding:utf-8

'''
ENONCE 4 Version: 
Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
Version 2 : en utilisant une boucle

'''
from os import system
from math import *

system("cls")
print("\n====================| EXERCICE 4 - VERSION 2 - TD1 |====================\n")
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

# BOUCLE PUISSANCE
if n < 0:
    puiss = 1 / (x**abs(n))
else:
    i = 1
    while i <= n:
        puiss = x*x
        i+=1

# CALCULS ET AFFICHAGE
print("\n====================>RESULTAT :<====================")
print("\n\t=>",x,"A LA PUISSANCE",n,"EST EGALE A: ",puiss)
print("\n\t=>",x,"A LA PUISSANCE",n,"EST EGALE A: ",puiss)
print("\n\t=> {0} A LA PUISSANCE {1} EST EGALE A: {2}".format(x,n,puiss))
print("\n====================================================\n")
system("pause")