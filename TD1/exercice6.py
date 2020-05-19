#coding: utf-8

'''
ENONCE 6 :
Faire un programme qui saisit les coordonnées de 2 points A (x1, y1) et b(x2, y2) et qui affiche la distance entre les
2 points.
Formule : distante = racine carrée de ((x1 – x2)2 + (y1 – y2)2)
Racine carrée : sqrt. Ex : sqrt(7) ; <math.h>

'''
import os
from math import *

os.system("cls")
print("\n====================| EXERCICE 6 - TD1 |====================\n")

valCorrect = False

# RECUPERATION & CONTROLE DES VALEURS SAISIES
while valCorrect == False:
    try:
        print("\n\t\t[COORD. DU POINT A]")
        x1 = float(input("\n--> VEUILLEZ ENTRER UN REEL X1: "))
        y1 = float(input("\n--> VEUILLEZ ENTRER UN REEL Y1: "))
        
        print("\n\t\t[COORD. DU POINT B]")
        x2 = float(input("\n--> VEUILLEZ ENTRER UN REEL X2: "))
        y2 = float(input("\n--> VEUILLEZ ENTRER UN REEL Y2: "))
        valCorrect = True
    except ValueError:
        print("!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
os.system("pause")

# CALCULS DE LA DISTANCE
dist = sqrt(pow((x1-x2),2) + pow((y1-y2),2))

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n-> La distance entre le point A et le point B est :",dist)
print("\n==========================================================================\n")
