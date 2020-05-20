#coding: utf-8

'''
ENONCE 14 : Faire un programme qui saisit une date (jour, mois et année) 
et qui indique si l’année est bissextile

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 14 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        jour = int(input("-> VEUILLEZ DONNER UN JOUR [1 .. 31]: "))
        mois = int(input("-> VEUILLEZ DONNER UN MOIS [1 .. 12]: "))
        annee = int(input("-> VEUILLEZ DONNER UNE ANNEE [1 .. xxxx]: "))
        assert (jour >= 1 and jour <= 31) and (mois >= 1 and mois <= 12) and (annee > 0)
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!\n")
        continue
    except AssertionError:
        print("\n\t!! LA DATE EST INCORRECTE !! REVOIR [JOUR ou MOIS ou ANNEE]!!\n")
    else:
        correct = True
print("")

# DETERMINATION & AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print(str.upper("\n\t\tL'année saisie est bissextile.\n"))
else:
    print(str.upper("\n\t\tL'année saisie n'est pas bissextile."))
print("\n==========================================================================\n")
os.system("pause")