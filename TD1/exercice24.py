#coding: utf-8

'''
ENONCE 24: Nombre secret : écrire un programme qui demande à l’utilisateur 1 d’entrer un nombre et à
l’utilisateur 2 de le trouver en affichant, à chaque tentative, « trop grand » si le nombre entré est plus grand que le
nombre secret, « trop petit » sinon. Le programme s’arrête quand l’utilisateur 2 a trouvé le nombre secret.
'''
import os

# STARTING OF THE PROGRAM
welcMsg = "\n\t\t--> WELCOME {0} TO THE GUESSING GAME <--\n".format(os.getlogin())
os.system("cls")
print("\n====================| EXERCICE 24 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        print("\n\t\t[(: SETTING UP THE SET BY USER 1:)]")
        a = int(input("-> VEUILLEZ SAISIR LE NOMBRE A DEVINER: "))
        # assert b != 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

#  STARTING THE GAME
nbr = None
cptT = 1
while a != nbr:
    try:
        print("\n\t\t--(TENTATIVE N° : ",cptT," USER 2)--")
        nbr = int(input("-> ENTREZ UN NOMBRE: "))
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        if nbr > a:
            print("\nLe Nombre cherché est PLUS PETIT que: \n",nbr)
        elif nbr < a:
            print("\nLe Nombre cherché est PLUS GRAND que: \n",nbr)
        else:
            print("\n==========================================================================\n")
            print("\n\n\t\t\t!!! BRAAAAVOOOOO !!!\n\t\t VOUS AVEZ DEVINEZ LE NOMBRE EN {} TENTATIVES !\n\n".format(cptT))
            print("\n==========================================================================\n")
        cptT += 1
        os.system("pause")

