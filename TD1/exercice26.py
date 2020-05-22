#coding: utf-8

'''
ENONCE 25: Nombre secret : écrire un programme qui demande à l’utilisateur 1 d’entrer un nombre et à
l’utilisateur 2 de le trouver en affichant, à chaque tentative, « trop grand » si le nombre entré est plus grand que le
nombre secret, « trop petit » sinon. Le programme s’arrête quand l’utilisateur 2 a trouvé le nombre secret.
'''
import os
import time

# STARTING OF THE PROGRAM
welcMsg = "\n\t\t--> HELLO {0} !!<--\n".format(os.getlogin())
os.system("cls")
os.system("color a")
print("\n====================| EXERCICE 26 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

# SIZE OF THE ARRAY/LIST
limit = 5   
# CREATION & REMPLISSAGE DE LA LISTE
tabVal = []# Liste Vide Agissant come un tableau
print("\n\t\t[(: REMPLISSAGE DE LISTE DES VALEURS :)]\n")
for i in range(0, limit):
    ok  = False
    while not(ok):
        try:
            print("\n\t\t\t[VALEUR N°",i+1,"]")
            tabVal.append(int(input("\n-> ENTRER UNE VALEUR : ")))
        except ValueError:
            print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        else:
            ok = True
print("")

# ANALYSE DU VECTEUR
for i in range(0, limit):
    if i < limit:
        if tabVal[i] > tabVal[i+1]:
            croissant = False
        elif tabVal[i] < tabVal[i+1]:
            decroissant = False

# AFFICHAGE DU RESULTAT
print("\n===============================>RESULTAT :<===============================\n")
if croissant and decroissant:
    print("\n\t➡ LA SUITE EST CONSTANTE !")
elif croissant and not(decroissant):
    print("\n\t➡ LA SUITE EST CROISSANT !")
elif not(croissant) and decroissant:
    print("\n\t➡ LA SUITE EST DECROISSANT !")
elif not(croissant) and not(decroissant):
    print("\n\t➡ LA SUITE EST QUELCONQUE !")
    pass
print("\n==========================================================================\n")
os.system("pause")