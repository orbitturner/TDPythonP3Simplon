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
print("\n====================| EXERCICE 25 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

print("\n===============================>RESULTAT :<===============================\n")
for i in range(0, 10):
    for j in range(0, i):
        print(i, end=" ")
        time.sleep(0.05)
        os.system("color a")
    print("")
print("\n==========================================================================\n")
os.system("pause")