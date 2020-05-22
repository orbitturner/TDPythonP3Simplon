#coding: utf-8

'''
ENONCE 18: Faire un programme qui calcule et affiche le PPCM de deux entiers saisis au clavier.
'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 18 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        a = int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: "))
        b = int(input("-> VEUILLEZ SAISIR UN DEUXIEME NOMBRE ENTIER: "))
        # assert b != 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

# SAUVEGARDE DES VALEURS INITIALES
c = a 
d = b
# CALCULS 
print("\n===============================>RESULTAT :<===============================\n")
while a != b:
    if a > b:
        b = b + d
    else:
        if a < b:
            a = a + c
    chaine = ("\t\t\t{:4} || {}".format(a, b))
    print(chaine.center(29," "))
    # print("\t\t\t",a," || ",b)

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t\tLE PPCM DE CES DE {} ET {} EST: {}\n".format(c, d, a))
print("\n==========================================================================\n")
os.system("pause")