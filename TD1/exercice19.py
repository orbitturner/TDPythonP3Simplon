#coding: utf-8

'''
ENONCE 19 : Ecrire l’algorithme qui affiche la somme des prix d'une suite d'articles en CFA (entiers) saisies par
l'utilisateur et se terminant par zéro.
'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 19 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
som = 0
i = 1
correct = False
while not(correct):
    try:
        print("\n\t\t[ARTICLE NUMERO",i,"]")
        prixArt = int(input("-> VEUILLEZ SAISIR LE PRIX DE L'ARTICLE : "))
        assert prixArt >= 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n!!LE PRIX DE L'ARTICLE NE PEU ETRE NEGATIF !!\n")
    else:
        if prixArt == 0:
            correct = True    
        else:
            som += prixArt
            i+=1
print("")

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t\tLA SOMME DES ARTICLES SAISIS EST: {0:4d}\n".format(som))
print("\n==========================================================================\n")
os.system("pause")
