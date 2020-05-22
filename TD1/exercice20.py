#coding: utf-8

'''
ENONCE 20: Ecrire un algorithme qui demande successivement 10 nombres à l'utilisateur, 
et qui affiche à la fin le plus grand de ces 10 nombres 
Et affiche aussi son rang dans la liste saisie
'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 20 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
pGrand = 0
i = 1
correct = False
while not(correct):
    try:
        print("\n\t\t[NOMBRE NUMERO",i,"]")
        nombre = int(input("-> VEUILLEZ SAISIR UN NOMBRE : "))
        assert nombre >= 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n!!LE NOMBRE NE PEUT ETRE NEGATIF !!\n")
    else:
        if i == 10:
            correct = True    
        else:
            if nombre > pGrand:
                pGrand = nombre
                pos = i
            i+=1
print("")

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t\t-> LePLUS GRAND NOMBRE SAISI EST: {0:4d}\n".format(pGrand))
print("\n\t\t-> SA POSITION EST: {0:4d}\n".format(pos))
print("\n==========================================================================\n")
os.system("pause")
