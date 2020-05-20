#coding: utf-8

'''
ENONCE 8 : Ecrire un algorithme permettant de résoudre une équation du second degré.
Ax2 + bx + c = 0

'''
import os
from math import *

# STARTING THE PROGRAM
loaded = True
while loaded:
    os.system("cls")
    print("\n====================| EXERCICE 8 - TD1 |====================\n")
    print("\t\t--> EQUATION DE LA FORME [ax^2 + bx + c = 0] <--")

    # RECUPERATION & CONTROLE DES VALEURS SAISIES
    correct = False
    while not(correct):
        try:
            a = float(input("-> VEUILLEZ DONNER LA VALEUR DE a: "))
            b = float(input("-> VEUILLEZ DONNER LA VALEUR DE b: "))
            c = float(input("-> VEUILLEZ DONNER LA VALEUR DE c: "))
        except ValueError:
            print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
            continue
        else:
            correct = True
    # SI ON A UN EQUATION DU PREMIER
    if a == 0:
        print("\n\t\t--> PASSAGE EN EQUATION DU PREMIER DEGRES[b est NUL] <--")
        print("\t\t--> EQUATION DE LA FORME [bx + c = 0] <--")
        if b != 0:
            print("\n\n-> LA SOLUTION DE L'EQUATION EST:",-c/b)
            os.system("pause")
        else:
            print("\n\n-> L'EQUATION N'ADMET PAS DE SOLUTION !")
            os.system("pause")
    else:
        # CALCULS DE DELTA
        delta = (b*b) - 4 * a * c
        racineDelta = sqrt(delta)
        # DETERMINATION DE LA SOLUTION DE L'EQUATION
        if delta > 0:
            print("\n===============================>RESULTAT :<===============================\n")
            print("\n\n-> L'EQUATION EST ADMET DEUX SOLUTIONS :")
            print("\n\t-> X1:",(-b-racineDelta)/(2*a))
            print("\n\t-> X2:",(-b+racineDelta)/(2*a))
            print("\n==========================================================================\n")
            os.system("pause")
        else:
            if delta == 0:
                print("\n===============================>RESULTAT :<===============================\n")
                print("\n\n-> LA SOLUTION DE L'EQUATION EST:",-b/(2*a))
                os.system("pause")
            else:
                print("\n===============================>RESULTAT :<===============================\n")
                print("\n\n-> L'EQUATION N'ADMET PAS DE SOLUTION REELLES !!")
                os.system("pause")

    # PROMPT BEFORE QUIT
    valide = False
    while not(valide):
        print("\n\n VOULEZ-VOUS CALCULER UNE AUTRE EQUATION ?")
        try:
            choice = int(input("\t\t? [ 1 --> OUI || 2 --> NON] ?\n"))
            assert choice > 0 and choice <3
        except ValueError:
            print("!! ENTREZ UN NOMBRE VALIDE ENTRE 1 & 2 !!")
        except AssertionError:
            print("\n\t\t!! CHOIX NON DISPONIBLE !!")
        else:
            valide = True
    if choice == 1:
        os.system("cls")
        continue
    else:
        os.system("cls")
        exit()