#coding: utf-8

'''
ENONCE 13 : Faire un programme qui saisit une date (jour, mois et année) 
et qui indique si la date est valide

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 13 - TD1 |====================\n")

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
if mois == 2 and jour > 29:
    print("\n\t\t!! LA DATE SAISIE EST INCORRECTE !!")
else:
    print("\n\t\t-> LA DATE SAISIE EST VALIDE <-")
