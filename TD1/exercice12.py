#coding: utf-8

'''
ENONCE 12 : Un nombre est parfait s’il est égal à la somme de ses diviseurs stricts (différents de lui-même). Ainsi
par exemple, l’entier 6 est parfait car 6 = 1 + 2 + 3. Écrire un algorithme permettant de déterminer si un entier
naturel est un nombre parfait.

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 12 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        nombre = abs(int(input("-> VEUILLEZ DONNER UN NOMBRE ENTIER: ")))

    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

# CALCULS & AFFICHAGE
cpt = 0
i = 1
while i <= nombre/2:
    if nombre % i == 0:
        cpt+=nombre
os.system("pause")
if cpt == nombre:
    print("\n===============================>RESULTAT :<===============================\n")
    print("\t\t LE NOMBRE",nombre,"EST UN NOMBRE PARFAIT")
    print("\n==========================================================================\n")
else:
    print("\n===============================>RESULTAT :<===============================\n")
    print("\t\t LE NOMBRE",nombre,"N'EST PAS UN NOMBRE PARFAIT")
    print("\n==========================================================================\n")
os.system("pause")