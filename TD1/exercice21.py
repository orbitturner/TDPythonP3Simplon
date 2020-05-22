#coding: utf-8

'''
ENONCE 21: Ecrire un algorithme mettant en œuvre le jeu suivant entre deux joueurs : Le premier utilisateur
saisi un entier que le second doit deviner. Pour cela, il a le droit à autant de tentatives qu'il souhaite. A chaque
échec, le programme lui indique si l'entier est plus grand ou plus petit que sa proposition. Un score est affiché
lorsque l'entier est trouvé.
'''
import os

# STARTING OF THE PROGRAM
welcMsg = "\n\t\t--> WELCOME TO THE GUESSING GAME <--\n"
os.system("cls")
print("\n====================| EXERCICE 21 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        print("\n\t\t[(: SETTING UP THE SET :)]")
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
        print("\n\t\t--(TENTATIVE N° : ",cptT,")--")
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

