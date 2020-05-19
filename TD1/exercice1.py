#coding:utf-8

'''
ENONCE : 
Ecrire un programme qui saisit deux entiers a et b, calcule et affiche le quotient entier, le reste de la division et le
ratio (quotient réel).
'''

import os

correctValue = False
os.system("cls")
print("\n====================| EXERCICE 1 - TD1 - DIVISION |====================\n")

# RECUPERATION ET CONTROLE DE LA SAISIE
while correctValue == False:
    try:
        a = int(input("\n==> ENTRER LE NOMBRE A : \n"))
        b = int(input("\n==> ENTRER LE NOMBRE B : \n"))
    except:
        print("!! VEUILLEZ ENTRER UN NOMBRE ENTIER VALIDE !!")
        a=0
        b = 0
        os.system("pause")
        os.system("cls")
        continue
    finally:
        if b != 0:
            correctValue = True
        else:
            print("\n!! LE NOMBRE B DOIT ETRE STRICTEMENT DIFFERENT DE 0 !!\n")

# CALCULS & AFFICHAGES
print("→ La QUOTIENT ENTIER de la division entre {0} ET {1} EST: {2}".format(a, b, a//b))
print("→ La RESTE de la division entre ",a ," ET ",b ," EST: ", a%b)
print("→ La QUOTIENT REEL de la division entre ",a ," ET ",b ," EST: ", a/b)
print("=================================================================================")

os.system("pause")
